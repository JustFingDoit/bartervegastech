"""
    Module for handlers.
"""
import logging
from pyramid_handlers import action
from pyramid.view import view_config

from pyramid.httpexceptions import HTTPBadRequest
from pyramid.httpexceptions import HTTPFound
from pyramid.httpexceptions import HTTPNotFound

#from bartervegastech.dbmodels.barterdb import get_player_ids, \
#        get_poker_player_by_id
from bartervegastech.dbmodels.barterdb import UserFactory, ListingFactory
#from bartervegastech.dbmodels.shirtsbyme import 

from formencode import Schema
from formencode import validators
from pyramid_simpleform import Form

import datetime, random


class BaseHandler(object):
    '''
        Base handler class. Sets up logging
    '''
    default_logger = logging.getLogger(__name__ + ".BaseHandler")
    request = None
    context = None

    def __init__(self, context, request):
        '''
            Initializes the logging, request, and context.
        '''
        self.default_logger.debug("in %s __init__" % self.__class__.__name__)
        self.log = logging.getLogger(__name__ + '.' + self.__class__.__name__)
        self.request = request
        self.context = context

class Listing(object):
    
    type = ''
    username = ''
    date = ''
    category = ''
    title = ''
    
    def __init__(self, type, username, date, category, title):
        self.title = title
        self.type = type
        self.date = str(date)[10:]
        self.category = category
        self.username = username

class PageHandler(BaseHandler):


    @action(renderer="home.mako")
    def home(self):
        ''' shows listing on home page '''
        self.log.debug("in home view")
        listFactory = ListingFactory()
        listings = listFactory.get_listings()
        lists = list()
        for each in listings:
            lists.append(Listing(each.offerwant, listFactory.get_username(each.user_id), 
                              each.created_on, listFactory.get_category(each.id), each.title))
        return {'listings': lists}
        
    @action(renderer="about.mako")
    def about(self):
        ''' returns an empty dict '''
        self.log.debug("in about view")
        return {}
        
    @action(renderer="users.mako")
    def users(self):
        ''' returns an empty dict '''
        self.log.debug("in about view")
        return {}

class LoggedInHandler(BaseHandler):
    '''
        Base handler implementing an __init__ that ensures there is a logged_in user.
    '''

    def __init__(self, context, request):
        '''
            Determines if the user should be redirected to the login page.
        '''
        super(LoggedInHandler, self).__init__(context, request)
        if request.session.get('logged_in') == None :
            if not 'login' in request.path :
                self.log.debug('not logged in raising exception')
                raise HTTPFound(location="/users/login")

    def delete(self):
        ''' delete the catalog found in matchdict's id'''
        id_ = self.request.POST.get('id')
        location = self.request.POST.get('location')
        self.log.debug('found id, and location %s, %s' % (id, location))
        if id_ == None or location == None:
            raise HTTPBadRequest()
        self.context.delete(int(id_))
        return HTTPFound(location=location)


class UserAccountHandler(LoggedInHandler):
    '''
        Handler that deals with user related views.
    '''

    @action(name="login", renderer="login.mako")
    def login(self):
        '''
            Log the user in, or return a failed message
        '''
        #from bartervegastech.dbmodels.barterdb import verify_user, get_user_id
        self.log.debug('in login view')
        username = ''
        password = ''
        message = ''
        if 'login_button' in self.request.params:
            username = self.request.params.get('username')
            password = self.request.params.get('password')
            try:           
                if self.context.verify_user(username, password):
                    self.request.session['logged_in'] = self.context.get_user_id(username)
                    self.log.debug("Login succeeded")
                    return HTTPFound(location = "/")
                self.log.debug("Login failed, but tried")
                message = "Login failed"
            except AssertionError:
                print "\n\nBBBBBBBBBBB"
                self.log.debug("Login failed")
                message = "Login failed."
        self.log.debug('login view returning')
        return {'username':username, 'password':password, 'message':message}

    @view_config(name="logout")
    def logout(self):
        '''
            log the user out
        '''
        del self.request.session['logged_in']
        return HTTPFound(location = "/")


    @action(name="list", renderer='users.mako')
    def list_users(self):
        '''
            return a list of all the users.
        '''
        #from bartervegastech.dbmodels.barterdb import list_users
        
        factory = UserFactory()
        return {'users': factory.list_users()}
        #return {'users':list(self.context)}

    @action(name="add", renderer='add_user.mako')
    def add_user(self):
        '''
            Add a user to the system.
        '''
        #factory = UserFactory()
        if 'username' in self.request.params:
            username = self.request.params.get('username')
            password = self.request.params.get('password')
            password2 = self.request.params.get('password2')
            self.log.debug("username is " + str(username))
            if password == password2:
                self.log.debug("creating user")
                self.context.create_user(username, password)
            return HTTPFound(location = "/users/list")
            
        return {}
    
    @action(name="delete", renderer='users.mako')
    def delete_user(self):
        '''
            Remove a user from the system.
        '''
        id_ = self.request.matchdict.get('id')
        if id_ :
            self.context.delete(id_[0])
    
        return HTTPFound(location = "/users/list")
        

