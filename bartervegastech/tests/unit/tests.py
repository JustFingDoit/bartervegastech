import unittest
from pyramid.config import Configurator
from pyramid import testing
from formencode.api import Invalid

def _initTestingDB(**settings):
    from sqlalchemy import create_engine
    from bartervegastech.models import initialize_sql
    engines = list()
    
    engines.append(create_engine('sqlite:///Test.db'))
    
    session = initialize_sql(engines, True)
    return [session, engines[0]]

class ManagerBase(object):
   
    def setUp(self):
        self.request = testing.DummyRequest()
        self.config = testing.setUp(request=self.request)
        set = _initTestingDB()
        self.session = set[0]
        self.engine1 = set[1]

    def tearDown(self):
        testing.tearDown()
        #self.session.remove()
        
class SchemaTestBase(ManagerBase):
    '''Base for what applies to testing most of the schemas'''
    schema = None
    
    def setUp(self):
        ManagerBase.setUp(self)

    def _get_validator(self, key):
        return self.schema.fields[key]

    def assert_validator_not_empty(self, name):
        validator = self._get_validator(name)
        self.assertTrue(validator.not_empty, "%s allows empty" % name)

    def assert_validator_min_length(self, name, min_length):
        validator = self._get_validator(name)
        self.assertEqual(validator.minLength, min_length)
        

class TestMyView(ManagerBase, unittest.TestCase):
    def setUp(self):
        #self.config = testing.setUp()
        #_initTestingDB()
        ManagerBase.setUp(self)

    def tearDown(self):
        testing.tearDown()

