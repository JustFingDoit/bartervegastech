import os
import sys

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
    'SQLAlchemy',
    "pymysql_sa",
    'transaction',
    'pyramid_tm',
    'pyramid_debugtoolbar',
    'pyramid_beaker',
    'pyramid_handlers',
    'pyramid_simpleform',
    'zope.sqlalchemy',
    'zope.interface>=3.8.0',
    'passlib',
    'py-bcrypt',
    'formencode',
    ]

if sys.version_info[:3] < (2,5,0):
    requires.append('pysqlite')

setup(name='BarterVegasTech',
      version='0.1',
      description='BarterVegasTech',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='BarterVegasTech',
      install_requires = requires,
      entry_points = """\
      [paste.app_factory]
      main = bartervegastech:main
      """,
      paster_plugins=['pyramid'],
      )

