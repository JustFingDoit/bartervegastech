import logging
import transaction

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Unicode

from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base, MetaData

from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import mapper

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base1 = declarative_base()
#metadata1 = MetaData()
#metadata2 = MetaData()
from dashboard.dbmodels.dashdb import UserFactory
logger = logging.getLogger(__name__)
"""class MyModel(Base2):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255), unique=True)
    value = Column(Integer)

    def __init__(self, name, value):
        self.name = name
        self.value = value"""

class AppRoot(object):
    '''
        Traversal application root object
    '''
    __name__ = None
    __parent__ = None

    def __init__(self, request):
        '''
            initialize the root with a users object
        '''
        self.request = request
        self.dict = {}
        self.dict['users'] = UserFactory()

    def __getitem__(self, key):
        logger.debug("AppRoot.__getitem__ called with key %s" % key)
        item = self.dict.get(key)
        logger.debug("returning %r" % item)
        return item

def root_factory(request):
    '''
        Get the factory for the traversal process.
    '''
    return AppRoot(request)

def populate():
    factory = UserFactory()
    factory.create_user("administrator", "delicious")

def initialize_sql(engines, test=False):
    from dashboard.dbmodels import dashdb
    DBSession.configure(bind=engines[0])
    Base1.metadata.bind = engines[0]
    if test:
        Base1.metadata.drop_all(engines[0])
    Base1.metadata.create_all(engines[0])
        
    try:
        populate()
    except IntegrityError:
        transaction.abort()

def appmaker(engines):
    initialize_sql(engines)
    return root_factory
