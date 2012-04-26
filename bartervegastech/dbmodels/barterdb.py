import logging
import transaction
from sqlalchemy import Column, ForeignKey, desc, func
from sqlalchemy.types import Integer, String, Unicode, Boolean, DateTime, Text
from sqlalchemy.types import SmallInteger
from sqlalchemy.exc import IntegrityError
from bartervegastech.models import Base1, DBSession

import datetime
from passlib.context import CryptContext
session = DBSession()
session.expire_on_commit = False

logger = logging.getLogger(__name__)

def string_safe(value):
    '''Replace empty strings with spaces.'''
    return value.replace(' ', '_')


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
    name = Column(Unicode(255), unique=True)
    _password = Column('password', Unicode(255))
    pwd_context = CryptContext(
        #replace this list with the hash(es) you wish to support.
        schemes=[ "bcrypt" ],
        default="bcrypt",
        )

    def __init__(self, name, password):
        ''' Initialize user with the given name and password '''
        self.name = name
        self.set_password(password)

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
    
    def __init__(self, user_id, category_id, offerwant, description)
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
    offerwant = Column(Integer)
    user_id = Column(Integer)

    def __init__(self, offerwant, user_id):
        self.created_on = datetime.datetime.now()    
        self.offerwant = offerwant
        self.user_id = user_id
        
class ListingMap(Base1, BaseObject):
    __tablename__ = 'listingsmap'
    id = Column(Integer, primary_key=True)
    listing_id = Column(Integer, ForeignKey('listings.id'))
    offerwant_id = Column(Integer, ForeignKey('offerswants.id'))
    
    def __init__(self, listing_id, offerwant_id):
        self.listing_id = listing_id
        self.offerwant_id = offerwant_id

    
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
        
    def create_user(self, name, password):
        """Create a new administrative user"""
        user = UserAccount(name, password)
        return self.add(user)
        
    def verify_user(self, name, password):
        """Authenticate user credentials"""
        try:
            user = session.query(UserAccount).filter_by(name = name).one()
        except:
            #No such user exists
            return False
        return user.validate_password(password)
        
    def list_users(self):
        """List all the users"""
        return session.query(UserAccount).all()
    
    def get_user_id(self, username):
        """Gets user id from username"""
        try:
            userid = session.query(UserAccount.id).filter_by(name = username).one()
        except:
            return None
        return userid

class OfferWantFactory(BaseFactory):
    '''
        Factory for offers and wants
    '''
    def __init__(self):
        """Initialize factory"""
        BaseFactory.__init__(self, OfferWant)

    def create_offer(self, category_id, offer):
        offer = OfferWant(user_id, category_id, "offer", offer)
        return self.add(offer)
    
    def create_want(self, category, want):
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
        
class ListingFactory(BaseFactory):
    '''
        Factory for listings
    '''
    def __init__(self):
        """Initialize factory"""
        BaseFactory.__init__(self, Listing)
    
    def get_listings_by_type(offerwant):
        '''
            Figure out all the listings of the specific type
            Then get all the details for that listing
        '''
        listings = self.filter_by(offerwant=offerwant).all()
        for each in listings:
            listing = session.query(ListingMap).filter_by(id=each.id).scalar()
            
    
    
    def get_