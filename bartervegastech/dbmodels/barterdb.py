import logging
import transaction
from sqlalchemy import Column, ForeignKey, desc, func
from sqlalchemy.types import Integer, String, Unicode, Boolean, DateTime, Text
from sqlalchemy.types import SmallInteger
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import relationship, backref
from bartervegastech.models import Base1, DBSession

import datetime
from passlib.context import CryptContext
session = DBSession()
session.expire_on_commit = False

logger = logging.getLogger(__name__)

def string_safe(value):
    '''Replace empty strings with spaces.'''
    return value.replace(' ', '_')


def gen_hash_password(password):
    """Generates a hashed password"""
    import random
    letters = 'abcdefghijklmnopqrstuvwxyz0123456789'
    p = ''
    random.seed()
    for x in range(32):
        p += letters[random.randint(0, len(letters)-1)]
    return p

def generate_password():
    """Generates a password"""
    import random
    import string
    random.seed(datetime.datetime.now())
    vc = string.ascii_letters + string.digits
    h1 = ''.join([random.choice(vc) for i in range(10)])
    return gen_hash_password(h1)


class BaseObject(object):
    '''
        A base object.
    '''

    def __init__(self, name):
        self.name = name

    @property
    def name_safe(self):
        ''' replace spaces with underscores '''
        return string_safe(self.name)

    def to_dict(self):
        ''' return a dict representation of the object'''
        props = self._remove_prop()
        return self._to_dict(props.iteritems())

    def _to_dict(self, properties):
        ''' private to dict '''
        items = {}
        for attr, value in properties:
            if str(attr) == 'parent':
                continue
            if not str(attr).startswith('_'):
                if isinstance(value, list):
                    new_value = []
                    for item in value:
                        new_value.append(item.to_dict())

                    value = new_value
                elif isinstance(value, BaseObject):
                    value = value.to_dict()
                items[attr] = value
        my_dict = {}
        my_dict[self.__class__.__name__] = items
        return my_dict

    def _remove_prop(self):
        ''' Remove the properties that are defined in backref_props'''
        import copy
        import inspect
        inspect.getmembers(self)
        props = copy.copy(self.__dict__)
        if hasattr(self, 'backref_props'):
            for name in self.backref_props:
                del props[name]
        return props

    def __str__(self):
        '''to string method'''
        props = self._remove_prop()
        string = "\n<" + __name__ + "." + self.__class__.__name__ + " "
        for attr, value in props.iteritems():
            if not str(attr).startswith('_'):
                string += "\n\t" + str(attr) + "=" + str(value) + " "
        string += ">"
        return string


class UserAccount(Base1, BaseObject):
    '''
        Ummmm. A user account class.
    '''
    __tablename__ = 'USER_ACCOUNT'
    id = Column(Integer, primary_key=True)
    username = Column(Unicode(255), unique=True)
    _password = Column('password', Unicode(255))
    email = Column(Text)
    activation = Column(Text)
    forgot = Column(Text)
    website = Column(Text)
    tagline = Column(Text)
    twitter = Column(Text)
    description = Column(Text)
    email_notification = Column(Boolean)
    listings = relationship("Listing", backref="user")
    replies = relationship("Reply", backref="user")
    pwd_context = CryptContext(
        #replace this list with the hash(es) you wish to support.
        schemes=[ "bcrypt" ],
        default="bcrypt",
        )

    def __init__(self, name, password, email):
        ''' Initialize user with the given name and password '''
        self.username = name
        self.set_password(password)
        self.email = email
        self.activation = generate_password()
        self.forgot = 0
        self.email_notification = 1

    def password(self):
        '''
            Returns the encrypted password.
        '''
        return self._password

    def set_password(self, pwd):
        '''
            Encrypts password on the fly.
        '''
        self._password = self.pwd_context.encrypt(pwd)
    
    def validate_password(self, password):
        """
            Check the password against existing credentials.
            this method returns a boolean.

            @param password: the password that was provided by the user to
            try and authenticate. This is the clear text version that we will
            need to match against the encrypted we store.
        """
        return self.pwd_context.verify(password, self.password())


class OfferWant(Base1, BaseObject):
    __tablename__ = 'offerswants'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('USER_ACCOUNT.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))
    offerwant = Column(Text)
    description = Column(Text)
    status = Column(Integer)
    
    def __init__(self, user_id, category_id, offerwant, description):
        self.user_id = user_id
        self.category_id = category_id
        self.offerwant = offerwant
        self.description = description
        self.status = 0

class Category(Base1, BaseObject):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    category = Column(Text)

    def __init__(self, category):
        self.category = category
        
class Listing(Base1, BaseObject):
    __tablename__ = 'listings'
    id = Column(Integer, primary_key=True)
    created_on = Column(DateTime)
    offerwant = Column(Text)
    user_id = Column(Integer, ForeignKey('USER_ACCOUNT.id'))
    title = Column(Text)
    private = Column(Boolean)

    def __init__(self, offerwant, user_id, title, private):
        self.created_on = datetime.datetime.now()    
        self.offerwant = offerwant
        self.user_id = user_id
        self.title = title
        self.private = private
        
class ListingMap(Base1, BaseObject):
    __tablename__ = 'listingsmap'
    id = Column(Integer, primary_key=True)
    listing_id = Column(Integer, ForeignKey('listings.id'))
    offerwant_id = Column(Integer, ForeignKey('offerswants.id'))
    
    def __init__(self, listing_id, offerwant_id):
        self.listing_id = listing_id
        self.offerwant_id = offerwant_id

class Reply(Base1, BaseObject):
    __tablename__ = 'replies'
    id = Column(Integer, primary_key=True)
    listing_id = Column(Integer, ForeignKey('listings.id'))
    user_id = Column(Integer, ForeignKey('USER_ACCOUNT.id'))
    description = Column(Text)
    
    def __init__(self, listingid, userid, description):
        self.listing_id = listingid
        self.user_id = userid
        self.description = description
    
class BaseFactory(object):
    '''
        Base factory providing basic CRUD operations.
    '''
    def __init__(self, type_):
        self.type = type_

    def __iter__(self):
        '''
            an iter view of my type
        '''
        return iter(self.get_query())

    def get_query(self):
        ''' Get a query of my type '''
        return session.query(self.type)

    def filter_by(self, **kwargs):
        '''Retrieve a query filtered by the kwargs '''
        query = self.get_query()
        return query.filter_by(**kwargs)

    def order_by_desc(self, **kwargs):
        '''Retrieve a query by a specific order'''
        query = self.get_query()
        return query.order_by(desc(**kwargs))
        

    def get(self, name):
        '''
            Get the product with the given name
        '''
        return self.filter_by(name=name).scalar()

    def get_by_id(self, id_):
        '''
            Retrieve the object with the given id.
        '''
        int_id = int(id_)
        return self.filter_by(id=int_id).scalar()

    def delete(self, id_):
        '''
            Delete the object with the given id.
        '''
        logger.debug("delete received id %s" % id_)
        object_ = self.get_by_id(id_)
        session.delete(object_)
        session.flush()
        transaction.commit()

    def add(self, object_):
        '''
            Add the given object to the system.
        '''
        if object is None:
            raise Exception('None type object received')

        id_ = None
        try:
            logger.debug('adding %s' % object_)
            session.add(object_)
            session.flush()
            id_ = object_.id
            transaction.commit()
        except IntegrityError:
            logger.critical('Error adding object %s' % object_)
            session.rollback()
            raise
        #return a *one* query to ensure the object is in the db
        logger.debug('id is %d' % id_)
        obj = self.filter_by(id=id_).one()
        logger.debug('returning object %s' % obj)
        return obj

    def new_object(self):
        ''' return an empty object of my type '''
        return self.type()

    def update(self, object_):
        ''' merges the object into session.'''
        id_ = object_.id
        transaction.begin()
        #session = DB_SESSION()
        session.merge(object_)
        session.flush()
        transaction.commit()
        return self.filter_by(id=id_).one()

class UserFactory(BaseFactory):
    '''
        Factory for users
    '''
    def __init__(self):
        """Initialize factory"""
        BaseFactory.__init__(self, UserAccount)
        
    def create_user(self, name, password, email):
        """Create a new administrative user"""
        user = UserAccount(name, password, email)
        return self.add(user)
        
    def verify_user(self, name, password):
        """Authenticate user credentials"""
        try:
            user = session.query(UserAccount).filter_by(username = name).one()
        except:
            #No such user exists
            return False
        return user.validate_password(password)
        
    def check_username(self, username):
        """Checks to see if username already exists"""
        user = self.filter_by(username=username).first()
        if user != None:
            return False
        return True
            
    def check_email(self, email):
        """Checks to see if email already exists"""
        user = self.filter_by(email=email).first()
        if user != None:
            return False
        return True
        
    def list_users(self):
        """List all the users"""
        return session.query(UserAccount).all()
    
    def get_user_id(self, username):
        """Gets user id from username"""
        try:
            user = self.filter_by(username = username).one()
        except:
            return None
        return user.id
    
    def activate(self, username, activation_code):
        ''' Activates the user's account
        returns boolean based on success '''
        id = self.get_user_id(username)
        if id != None:
            user = self.get_by_id(id)
            if user.activation == activation_code:
                user.activation = 1
                self.update(user)
                return True
        return False
    
    def get_user_by_email(self, email):
        try:
            user = self.filter_by(email=email).one()
        except:
            return None
        return user
        
    def forgot(self, id):
        user = self.get_by_id(id)
        user.forgot = generate_password()
        self.update(user)
        return user.forgot
    
    def resetcheck(self, username, code):
        user = self.get_by_id(self.get_user_id(username))
        if user.forgot == code:
            return True
        return False
    
    def reset(self, code, password):
        user = self.filter_by(forgot=code).scalar()
        if user != None:
            user.set_password(password)
            return True
        return False

class OfferWantFactory(BaseFactory):
    '''
        Factory for offers and wants
    '''
    def __init__(self):
        """Initialize factory"""
        BaseFactory.__init__(self, OfferWant)

    def create_offer(self, user_id, category_id, offer):
        offer = OfferWant(user_id, category_id, "offer", offer)
        return self.add(offer)
    
    def create_want(self, user_id, category_id, want):
        want = OfferWant(user_id, category_id, "want", want)
        return self.add(want)
        
        
class CategoryFactory(BaseFactory):
    '''
        Factory for categories
    '''
    def __init__(self):
        """Initialize factory"""
        BaseFactory.__init__(self, Category)
    
    def create_category(self, category):
        cat = Category(category)
        return self.add(cat)
        
    def get_by_category(self, name):
        '''
            Get the category by name
        '''
        return self.filter_by(category=name).scalar()
    
    def list_categories(self):
        return self.get_query().all()
        
class ListingFactory(BaseFactory):
    '''
        Factory for listings
    '''
    def __init__(self):
        """Initialize factory"""
        BaseFactory.__init__(self, Listing)
        
    def create_listing(self, offerwant, user_id, title, private):
        listing = Listing(offerwant, user_id, title, private)
        return self.add(listing)
    
    def create_map(self, listing_id, offerwant_id):
        map = ListingMap(listing_id, offerwant_id)
        try:
            session.add(map)
            session.flush()
            id_ = map.id
            transaction.commit()
        except IntegrityError:
            logger.critical('Error adding object %s' % map)
            session.rollback()
            raise
        return id_
    
    def create_reply(self, listing_id, user_id, desc):
        reply = Reply(listing_id, user_id, desc)
        if reply is None:
            raise Exception('None type object received')

        id_ = None
        try:
            logger.debug('adding %s' % object_)
            session.add(reply)
            session.flush()
            id_ = reply.id
            transaction.commit()
        except IntegrityError:
            logger.critical('Error adding object %s' % object_)
            session.rollback()
            raise
        return session.query(Reply).get(id_)
    
    def get_replies(self, listing_id):
        replies = session.query(Reply).filter_by(listing_id=listing_id).all()
        return replies
    
    def get_listings_by_type(offerwant):
        '''
            Figure out all the listings of the specific type
            Then get all the details for that listing
        '''
        listings = self.filter_by(offerwant=offerwant).all()
        #for each in listings:
        #    listing = self.filter_by(id=each.id).scalar()
        return listings
    
    def get_listings_match(self, type, userid):
        return self.filter_by(offerwant=type).filter_by(user_id=userid).all()
            
    def get_listings_by_user_id(self, id):
        '''
            Figure out all the listings of the specific type
            Then get all the details for that listing
        '''
        return self.filter_by(user_id=id).all()
            
    def get_listings(self):
        '''
            Just gets all the listings arranged by date DESC
            TODO change from 30 and handle pagination in the handler
        '''
        #return session.query(Listing).order_by(desc(Listing.created_on)).limit(30).all()
        query = self.get_query()
        #return self.order_by_desc(Listing.created_on).limit(30).all()
        return query.order_by(desc(Listing.created_on)).limit(30).all()
    
    def get_username(self, user_id):
        '''
            Returns the username from the user_id
        '''
        #listing = self.get_by_id(user_id)
        return session.query(UserAccount).get(user_id).username
    
    def get_offerwant(self, id):
        #First figure out if it's offer or want
        listing = self.get_by_id(id)
        map = session.query(ListingMap).filter_by(listing_id=listing.id).all()
        offerwantFactory = OfferWantFactory()
        offerwant_id = 0
        for each in map:
            if offerwantFactory.get_by_id(each.offerwant_id).offerwant == listing.offerwant:
                offerwant_id = each.offerwant_id
                break
        else:
            return None
        #Then get category for the associated offerwant
        return session.query(OfferWant).get(offerwant_id)
    
    def get_category(self, id):
        '''
            Using listing_id get the category
        '''
        offerwant = self.get_offerwant(id)
        if offerwant != None:
            return session.query(Category).get(offerwant.category_id).category
        return None
    
    def get_description(self, id):
        '''
            Get description of a listing by id
        '''
        offerwant = self.get_offerwant(id)
        if offerwant != None:
            return offerwant.description
        return None
        
    def get_inreturn(self, id):
        listing = self.get_by_id(id)
        map = session.query(ListingMap).filter_by(listing_id=listing.id).all()
        offerwantFactory = OfferWantFactory()
        offerwant_id = 0
        for each in map:
            if offerwantFactory.get_by_id(each.offerwant_id).offerwant != listing.offerwant:
                offerwant_id = each.offerwant_id
                break
        else:
            return None
        #Then get category for the associated offerwant
        offerwant = session.query(OfferWant).get(offerwant_id)
        if offerwant != None:
            return offerwant.description
        return None
    
    def remove(self, id):
        self.delete(id)
        map = session.query(ListingMap).filter_by(listing_id=id).all()
        for each in map:
            offerwant = session.query(OfferWant).get(each.offerwant_id)
            session.delete(offerwant)
            session.delete(each)
            session.flush()
            transaction.commit()
