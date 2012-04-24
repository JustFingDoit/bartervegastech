#!/usr/bin/env python
import unittest
from tests import ManagerBase
from pyramid import testing
from pyramid.httpexceptions import HTTPFound

#from mocks import MockCategoryFactory
from mock import MockFactory
from mock import MockUserFactory


class HandlerBase(ManagerBase):
    def _get_request(self, params=None, environ=None, headers=None, path='/',
                     cookies=None, post=None, **kw):
        return testing.DummyRequest(
                params=params,
                environ=environ,
                headers=headers,
                path=path,
                cookies=cookies,
                post=post,
                **kw
                )

    def _get_logged_in_request(self, params=None, environ=None, headers=None,
                               path='/', cookies=None, post=None, **kw):
        request = self._get_request(
                params=params,
                environ=environ,
                headers=headers,
                path=path,
                cookies=cookies,
                post=post,
                **kw
                )
        request.session['logged_in'] = 1
        return request

    def _assert_response_has_form(self, response):
        self.assertIsNotNone(response.get('form'), "No form found in response")



class TestLoggedInHandler(HandlerBase, unittest.TestCase):

    def _get_handler(self, params=None, post=None, context=MockFactory()):
        from dashboard.views.handlers import LoggedInHandler
        request = self._get_logged_in_request(params=params, post=post)
        #token = request.session.new_csrf_token()
        #request.POST['_csrf'] = token
        return LoggedInHandler(context, request)

    def test_constructor_not_logged_in(self):
        from dashboard.views.handlers import LoggedInHandler
        request = self._get_request()
        context = testing.DummyResource()
        self.assertRaises(HTTPFound, LoggedInHandler, context, request)

    def test_delete_no_id(self):
        params = {
            'location': '/foo'
        }
        from pyramid.httpexceptions import HTTPBadRequest
        handler = self._get_handler(post=params)
        self.assertRaises(HTTPBadRequest, handler.delete)

    def test_delete_no_location(self):
        params = {
            'id': '1'
        }
        from pyramid.httpexceptions import HTTPBadRequest
        handler = self._get_handler(post=params)
        self.assertRaises(HTTPBadRequest, handler.delete)

    def test_delete_returns_proper_location(self):
        params = {
            'location': '/foo/bar',
            'id': '1'
        }
        handler = self._get_handler(post=params)
        response = handler.delete()
        self.assertEqual('/foo/bar', response.location)


class FixtureBase(HandlerBase):
    def setUp(self):
        super(HandlerBase, self).setUp()
        from fixture import SQLAlchemyFixture
        from fixture.style import NamedDataStyle
        from productmanager.app import models

        self.dbfixture = SQLAlchemyFixture(
            env=models,
            engine=self.engine,
            style=NamedDataStyle()
        )

class TestUserAccountHandler(HandlerBase, unittest.TestCase):

    def setUp(self):
        ManagerBase.setUp(self)
        from pyramid_beaker import session_factory_from_settings

        self.config.testing_securitypolicy(userid='root', groupids=[])

        settings = {
            'session.auto': 'true',
            'session.key': 'foo',
            'session.type': 'file',
            'session.data_dir': '%(here)s/data/sessions/data',
            'session.lock_dir': '%(here)s/data/sessions/lock',
            'session.secret': 'myNotSoSecretSecret',
            'session.cookie_on_exception': 'true',
            }
        session_factory = session_factory_from_settings(settings)
        self.config.set_session_factory(session_factory)

    def test_login_view_success(self):
        from dashboard.dbmodels.dashdb import UserFactory
        handler = self._get_handler(params=self._get_params(),
                                    path='/users/login',
                                    context=UserFactory())
        handler.login()
        assert (self.request.session['logged_in'])[0] == 1

    def test_login_view_bad_user(self):
        from dashboard.views.handlers import UserAccountHandler
        from dashboard.dbmodels.dashdb import UserFactory

        params = self._get_params(username=u'foo')
        request = self._get_request(params=params, path='/users/login')
        context = UserFactory()
        handler = UserAccountHandler(context, request)
        response = handler.login()
        self.assertEquals(request.session.get('logged_in'), None)
        self.assertEquals(response["message"], "Login failed")
        self.assertEquals(response['username'], params['username'])
        self.assertEquals(response['password'], params['password'])

    def test_login_view_assertion_error(self):
        from dashboard.views.handlers import UserAccountHandler
        from dashboard.dbmodels.dashdb import UserFactory

        params = self._get_params(username=u'')
        request = self._get_request(path='/users/login')
        context = UserFactory()
        handler = UserAccountHandler(context, request)
        response = handler.login()
        self.assertEquals(request.session.get('logged_in'), None)
        self.assertEquals(response['username'], '')
        self.assertEquals(response['password'], '')
        self.assertEquals(response["message"], "Login failed.")
        

    def test_logout(self):
        handler = self._get_logged_in_handler()
        handler.logout()
        self.assertEquals(self.request.session.get('logged_in'), None)

    def test_list_users(self):
        from dashboard.views.handlers import UserAccountHandler
        from dashboard.dbmodels.dashdb import UserFactory
        request = self._get_logged_in_request()
        context = UserFactory()
        handler = UserAccountHandler(context, request)

        expected = list(context)
        response = handler.list_users()
        actual = response['users']
        self.assertEquals(actual, expected)

    def test_add_user_calls_create_user(self):
        params = self._get_params(username='bob2', password='neil')
        context = MockUserFactory()
        handler = self._get_handler(params=params,
                                    context=context,
                                    logged_in=True)
        self.assertIsNone(context.get(params['username']))
        handler.add_user()
        params = self._get_params(username='Ben', password='neil')
        self.assertIsNotNone(context.get(params['username']))

    def test_delete_user_calls_user_factory(self):
        params = self._get_params(username='bob2', password='neil')
        context = MockUserFactory()
        handler = self._get_handler(params=params,
                                    context=context,
                                    logged_in=True)
        
        handler.add_user()
        added_user_length = len(list(context))
        '''create a new params with matchdict'''
        user = context.get(params['username'])
        matchdict = {'id': (user.id,)}
        handler.request.matchdict = matchdict
        #should use the same request params
        handler.delete_user()
        deleted_user_length = len(list(context))
        self.assertEquals(added_user_length - 1, deleted_user_length)

    def _get_handler(self, params=None, environ=None, headers=None, path='/',
                     cookies=None, post=None,
                     context=testing.DummyResource(), **kw):
        '''TODO: REMOVE THIS and use the base impl '''
        if kw.get('logged_in'):
            self.request = self._get_logged_in_request(
                params=params,
                environ=environ,
                headers=headers,
                path=path,
                cookies=cookies,
                post=post,
                **kw
                )
        else:
            self.request = self._get_request(
                params=params,
                environ=environ,
                headers=headers,
                path=path,
                cookies=cookies,
                post=post,
                **kw
                )
        from dashboard.views.handlers import UserAccountHandler
        return UserAccountHandler(context, self.request)

    def _get_logged_in_handler(self):
        from dashboard.views.handlers import UserAccountHandler
        self.request = self._get_logged_in_request()
        context = testing.DummyResource()
        return UserAccountHandler(context, self.request)

    def _get_params(self, username=u'administrator', password=u'delicious',
                    login_button='Log in!'):
        return dict(
            username=username,
            password=password,
            password2=password,
            login_button=login_button,
        )
