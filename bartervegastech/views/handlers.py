"""
    Module for handlers.
"""
import logging
from pyramid_handlers import action
from pyramid.view import view_config
from pyramid.renderers import render

from pyramid.httpexceptions import HTTPBadRequest
from pyramid.httpexceptions import HTTPFound
from pyramid.httpexceptions import HTTPNotFound

#from bartervegastech.dbmodels.barterdb import get_player_ids, \
#        get_poker_player_by_id
from bartervegastech.dbmodels.barterdb import UserFactory, ListingFactory
#from bartervegastech.dbmodels.shirtsbyme import 

import formencode
from formencode import Schema
from formencode import validators
from formencode import htmlfill
from pyramid_simpleform import Form

import datetime, random

def sendMail(request, msg, to, username='', confirm=''):
    from pyramid_mailer import get_mailer
    from pyramid_mailer.message import Message
    mailer = get_mailer(request)
    if msg == 'confirm':
        message = Message(sender="noreply@bartervegastech.com", recipients=[to], 
                          subject="Welcome to BarterVegasTech!")
        message.body = "Hello " + username + ",\n\n" + \
            "Thank you for checking out http://www.bartervegastech.com\n\n" + \
            "To activate your account please go to:\nhttp://www.bartervegastech.com/message/" + \
            "activate/" + username + "/" + confirm + "\n\nIf you do not wish to have an " + \
            "account you may just ignore this email.\nThanks!\nBarterVegasTech.com"
        if request.registry.settings['testing'] != "true":
            mailer.send(message) 
    elif msg == 'forgot':
        message = Message(sender="support@bartervegastech.com", recipients=[to], 
                          subject="BarterVegasTech Password Recovery")
        message.body = "Hello " + username + ",\n\n" + \
            "To reset your password please go to:\nhttp://www.bartervegastech.com/reset/" + \
            username + "/" + confirm + "\n\n" + \
            "If you did not request to have your password changed then " + \
            "you may just ignore this email.\nThanks!\nBarterVegasTech.com"
        if request.registry.settings['testing'] != "true":
            mailer.send(message)
        

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



    def _get_signup_form(self):
        ''' get the form '''
        return Form(self.request, schema=UserSchema)

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
        ''' Shows the about page '''
        self.log.debug("in about view")
        return {}
        
    @action(name='users', renderer="users.mako", request_method='POST')
    def users_post(self):
        ''' creates a new user account or returns page with errors '''
        self.log.debug("in about view")
        #TODO set up CSRF token
        try:
            form_result = UserSchema().to_python(self.request.POST)
        except formencode.Invalid, error:
            form_result = error.value
            form_errors = error.error_dict or {}
            html = render('signup_form.mako', {})
            signupform = htmlfill.render(html, defaults=form_result, errors=form_errors)
            return {'signupform': signupform}
        if self.request.POST.get('password') == self.request.POST.get('confirm'):
            userFactory = UserFactory()
            usernamecheck = userFactory.check_username(self.request.POST.get('username'))
            emailcheck = userFactory.check_email(self.request.POST.get('email'))
            if usernamecheck and emailcheck:
                user = userFactory.create_user(self.request.POST.get('username'), 
                            self.request.POST.get('password'), self.request.POST.get('email'))
                sendMail(self.request, 'confirm', user.email, user.username, user.activation)
            else:
                if not usernamecheck:
                    form_errors={'username': "Username taken"}
                if not emailcheck:
                    form_errors['email'] = "Email address already used"
                return {'items': items, 'signupform': htmlfill.render(render('signup_form.mako', {}), 
                                defaults=form_result, errors=form_errors)}
        else:
            return {'signupform': htmlfill.render(render('signup_form.mako', {}), 
                                defaults=form_result, errors={'confirm': "Passwords didn't match"})}
           
        return HTTPFound(location='/message/confirm')
        
    
    @action(name='users', renderer="users.mako", request_method='GET')
    def users(self):
        html = render('signup_form.mako', {})
        signupform = htmlfill.render(html, errors={})
        return {'signupform': signupform}
    
    
    @action(renderer="message.mako")
    def message(self):
        id_ = self.request.matchdict.get('id')
        message = ''
        if id_ :
            if id_[0] == "confirm":
                message = "Thank you for signing up. Please check your email to activate your account."
            elif id_[0] == "activate":
                userFactory = UserFactory()
                if userFactory.activate(id_[1], id_[2]):
                    message = "Your account has been successfully activated. You may now login"
                else:
                    message = "There was an error activating your account. It may already be active or username no longer exists."
            elif id_[0] == "error":
                message = "An unknown error occurred."
        return {'message': message}
        
    @action(renderer="account.mako")
    def account(self):
        return{}

    @action(renderer="message.mako")
    def forgot(self):
        if self.request.POST.get('email'):
            userFactory = UserFactory()
            emailcheck = userFactory.check_email(self.request.POST.get('email'))
            if not emailcheck:
                message = "Email not found in our system."
            else:
                user = userFactory.get_user_by_email(self.request.POST.get('email'))
                code = userFactory.forgot(user.id)
                sendcode(self.request, forgot, email, user.username, code)
        else:
            message = "Please enter a valid email address."        
                

    @action(renderer="changepassword.mako")
    def reset(self):
        id_ = self.request.matchdict.get('id')
        userFactory = UserFactory()
        if id_:   
            if userFactory.resetcheck(id_[0], id_[1]):
                return {}
        return HTTPFound(location='/message/error')
            

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
            return HTTPFound(location = "/users")
            
        return {}
    
    @action(name="delete", renderer='users.mako')
    def delete_user(self):
        '''
            Remove a user from the system.
        '''
        if self.request.session.get('logged_in') == 1:
            id_ = self.request.matchdict.get('id')
            if id_ :
                self.context.delete(id_[0])
    
        return HTTPFound(location = "/users/list")
        

class UserSchema(Schema):
    '''Schema for Users'''
    allow_extra_fields = True
    username = validators.MinLength(3, not_empty=True)
    email = validators.Email(not_empty=True)
    password = validators.MinLength(6, not_empty=True)
    confirm = validators.MinLength(6, not_empty=True)
    
    
class OfferWant(Schema):
    '''Schema for creating an offer or want'''
    allow_extra_fields = True

class Profile(Schema):
    '''Schema for editing user profile'''
    allow_extra_fields = True