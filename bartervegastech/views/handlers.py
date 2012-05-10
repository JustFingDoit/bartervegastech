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
from bartervegastech.dbmodels.barterdb import UserFactory, ListingFactory, CategoryFactory
from bartervegastech.dbmodels.barterdb import OfferWantFactory
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
    elif msg == 'reply':
        message = Message(sender="support@bartervegastech.com", recipients=[to], 
                          subject="BarterVegasTech Reply")
        message.body = "Hello!\n\n" + \
            "You recieved a reply to your post: " + username + \
            "\n\nVisit " + confirm + " to view it.\n\n" + \
            "To change your email notification settings visit http://www.bartervegastech.com/account#profiletab"
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
        

class ShowListing(object):
    from bartervegastech.dbmodels.barterdb import UserAccount
    
    list_id = 0
    type = ''
    username = ''
    date = ''
    category = ''
    title = ''
    url = ''
    description = ''
    inreturn = ''
    user = object()
    
    
    def __init__(self, id, type, username, date, category, title):
        self.list_id = id
        self.title = title
        self.type = type
        self.date = str(date)[:10]
        self.category = category
        self.username = username
        self.user = UserFactory().get_user_by_username(username)
        self.url = '/' + type + '/' + username + '/' + self.date + '/' + cleanwords(category) + \
                '/' + cleanwords(title) 

def cleanwords(thestring):
    import re
    return re.sub(r"\s+", '-', thestring).lower()
    

def match(offerwant, username, date, category, title):
    '''Find a match for the listing that meets the criteria'''
    userFactory = UserFactory()
    user_id = userFactory.get_user_id(username)
    listFactory = ListingFactory()
    listings = listFactory.get_listings_match(offerwant, user_id)
    for each in listings:
        if title == cleanwords(each.title):
            return each
    return None

def get_listing(listing_id):
    listFactory = ListingFactory()
    listing = listFactory.get_by_id(listing_id)
    list = ShowListing(listing.id, listing.offerwant, listFactory.get_username(listing.user_id), 
                          listing.created_on, listFactory.get_category(listing.id), listing.title)
    list.description = listFactory.get_description(listing_id)
    list.inreturn = listFactory.get_inreturn(listing_id)
    return list

def get_listings(listings, listFactory):
    lists = list()
    for each in listings:
        lists.append(ShowListing(each.id, each.offerwant, listFactory.get_username(each.user_id), 
                          each.created_on, listFactory.get_category(each.id), each.title))
    return lists

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
        lists = get_listings(listings, listFactory)
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
                    message = "Your account has been successfully activated. You may now login."
                else:
                    message = "There was an error activating your account. It may already be active or username no longer exists."
            elif id_[0] == "nonactive":
                message = "Please activate your account with the url sent to your email address."
            elif id_[0] == "error":
                message = "An unknown error occurred."
        return {'message': message}
        
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
        return {'message': message}
                

    @action(renderer="pwreset.mako")
    def reset(self, message=""):
        id_ = self.request.matchdict.get('id')
        userFactory = UserFactory()
        if id_:   
            if userFactory.resetcheck(id_[0], id_[1]):
                return {'message': message}
        return HTTPFound(location='/message/error')
    
    @action(name="reset", renderer="message.mako", request_method='POST')
    def reset_post(self):
        code = self.request.params.get('code')
        password = self.request.params.get('password')
        confirm = self.request.params.get('confirm')
        if password != confirm:
            self.reset("Passwords don't match")
        userFactory = UserFactory()
        if userFactory.reset(code, password):
            message = "Password changed, you may login now."
        else:
            message = "There was an error changing your password" 
        return {'message': message}
    
    @action(renderer="info.mako")
    def offer(self):
        id_ = self.request.matchdict.get('id')
        username = id_[0]
        date = id_[1]
        category = id_[2]
        title = id_[3]
        list_match = match("offer", username, date, category, title)
        listing_id = list_match.id
        listing = get_listing(listing_id)
        if 'reply' in self.request.POST:
            description = self.request.POST['description']
            ListingFactory().create_reply(listing_id, self.request.session['logged_in'], 
                                          description)
            #check to see if poster is to be notified by email
            list_match = ListingFactory().get_by_id(listing_id)
            if list_match.user.email_notification:
                sendMail(self.request, "reply", list_match.user.email, listing.title, listing.url)
        replies = list()
        if not list_match.private or self.request.session.get('logged_in') == list_match.user.id: 
            replies = ListingFactory().get_replies(listing_id)
        elif self.request.session.get('logged_in') != None:
            #get replies that user wrote
            replies = ListingFactory().get_my_replies(self.request.session['logged_in'], listing_id)
        return {'listing': listing, 'replies': replies, 'private': list_match.private}
        
    @action(renderer="info.mako")
    def want(self):
        id_ = self.request.matchdict.get('id')
        username = id_[0]
        date = id_[1]
        category = id_[2]
        title = id_[3]
        list_match = match("want", username, date, category, title)
        listing_id = list_match.id
        listing = get_listing(listing_id)
        if 'reply' in self.request.POST:
            description = self.request.POST['description']
            ListingFactory().create_reply(listing_id, self.request.session['logged_in'], 
                                          description)
            #check to see if poster is to be notified by email
            list_match = ListingFactory().get_by_id(listing_id)
            if list_match.user.email_notification:
                sendMail(self.request, "reply", list_match.user.email, listing.title, listing.url)
        replies = list()
        if not list_match.private or self.request.session.get('logged_in') == list_match.user.id: 
            replies = ListingFactory().get_replies(listing_id)
        elif self.request.session.get('logged_in') != None:
            #get replies that user wrote
            replies = ListingFactory().get_my_replies(self.request.session['logged_in'], listing_id)
        return {'listing': listing, 'replies': replies, 'private': list_match.private}

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
        else:
            user = UserFactory().get_by_id(request.session['logged_in'])
            if user.activation != '1':
                if not 'login' in request.path and not 'logout' in request.path:
                    raise HTTPFound(location="/message/nonactive")

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
        if 'loginsubmit' in self.request.params:
            username = self.request.params.get('username')
            password = self.request.params.get('password')
            userFactory = UserFactory()
            if userFactory.verify_user(username, password):
                self.request.session['logged_in'] = userFactory.get_user_id(username)
                self.log.debug("Login succeeded")
                return HTTPFound(location = "/account")
            self.log.debug("Login failed, but tried")
            message = "Login failed"
        self.log.debug('login view returning')
        return {'username':username, 'password':password, 'message':message}

    @view_config(name="logout")
    def logout(self):
        '''
            log the user out
        '''
        del self.request.session['logged_in']
        return HTTPFound(location = "/")

    @action(renderer="message.mako", request_method='POST')
    def remove(self):
        id_ = self.request.matchdict.get('id')
        to_remove = id_[0]
        listFactory = ListingFactory() 
        listing = listFactory.get_by_id(to_remove)
        if listing.user_id == self.request.session['logged_in']:
            #User has permission to delete
            listFactory.remove(to_remove)
            message = "Successfully removed."
        else:
            message = "You do not have permission to delete this."
        return {'message': message}

    @action(renderer="account.mako")
    def account(self):
        listFactory = ListingFactory()
        listings = listFactory.get_listings_by_user_id(self.request.session['logged_in'])
        active = get_listings(listings, listFactory)
        categs = CategoryFactory()
        userFactory = UserFactory()
        user = userFactory.get_by_id(self.request.session['logged_in'])
        form = None
        if self.request.session.get('createform') != None:
            form = self.request.session['createform']
            del self.request.session['createform']
        if form == None:
            html = render('create_post.mako', {'categories': categs.list_categories()})
            form = htmlfill.render(html, errors={})
        profile_form = render('profile.mako', {'user': user})
        print "\n\n\n\nLogged in id"
        print self.request.session['logged_in']
        print "\n\n\n\n"
        return{'active': active, 'user': user, 'createpost' : form, 'profile': profile_form}

    @action(name='account', renderer="message.mako", request_method='POST')
    def account_post(self):
        if 'edit-profile-submit' in self.request.POST:
            form_result = ProfileSchema().to_python(self.request.POST)
            userFactory = UserFactory()
            user = userFactory.get_by_id(self.request.session['logged_in'])
            user.website = form_result['website']
            user.tagline = form_result['tagline']
            user.twitter = form_result['twitter']
            user.description = form_result['description']
            user.email_notification = form_result['emailnotification']
            userFactory.update(user)
            return HTTPFound(location="/account#profiletab")
        if 'submit-btn' not in self.request.POST:
            return HTTPFound(location="/account")
        try:
            form_result = OfferWantSchema().to_python(self.request.POST)
        except formencode.Invalid, error:
            form_result = error.value
            form_errors = error.error_dict or {}
            categs = CategoryFactory()
            html = render('create_post.mako', {'categories': categs.list_categories()})
            createform = htmlfill.render(html, defaults=form_result, errors=form_errors)
            self.request.session['createform'] = createform
            return HTTPFound(location='/account')
        listFactory = ListingFactory()
        user_id = self.request.session['logged_in']
        listing = listFactory.create_listing(form_result['status'], user_id,  
                                             form_result['title'], form_result['private'])
        offerwant = OfferWantFactory()
        offer = 0
        want = 0
        if form_result['status'] == "offer":
            offer = offerwant.create_offer(user_id,  
                                           form_result['category'], form_result['description'])
            want = offerwant.create_want(user_id, 
                                         0, form_result['inreturn'])
        elif form_result['status'] == "want":
            offer = offerwant.create_offer(user_id, 
                                           0, form_result['inreturn'])
            want = offerwant.create_want(user_id, 
                                         form_result['category'], form_result['description'])
        listFactory.create_map(listing.id, offer.id)
        listFactory.create_map(listing.id, want.id)
        message = "Your post has been created!"
        return {'message': message}


        
    #@action("want" renderer="info.mako", request_method="POST")
    #def 

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
            email = self.request.params.get('email')
            self.log.debug("username is " + str(username))
            if password == password2:
                self.log.debug("creating user")
                self.context.create_user(username, password, email)
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
    
    
class OfferWantSchema(Schema):
    '''Schema for creating an offer or want'''
    allow_extra_fields = True
    status = validators.MinLength(1, not_empty=True)
    title = validators.MinLength(3, not_empty=True)
    category = validators.Int()
    description = validators.MinLength(3, not_empty=True)
    inreturn = validators.MinLength(3, not_empty=True)
    private = validators.Bool()
    
class ProfileSchema(Schema):
    '''Schema for editing user profile'''
    allow_extra_fields = True
    username = validators.String()
    website = validators.String()
    tagline = validators.String()
    twitter = validators.String()
    description = validators.String()
    emailnotification = validators.Bool()
    
