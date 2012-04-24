from pyramid.config import Configurator
from pyramid_beaker import session_factory_from_settings
from sqlalchemy import engine_from_config

from bartervegastech.models import appmaker

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engines = list()
    engines.append(engine_from_config(settings, 'sqlalchemy.'))
    the_root = appmaker(engines)
    session_factory = session_factory_from_settings(settings)
    config = Configurator(settings=settings, root_factory=the_root)
    config.set_session_factory(session_factory)
    #config.add_static_view('static', 'dashboard:static', cache_max_age=3600)
    config.add_static_view('images', 'dashboard:static/images')
    config.add_static_view('css', 'dashboard:static/css')
    config.add_static_view('js', 'dashboard:static/js')
    #config.add_route('home', '/')
    #config.add_view('dashboard.views.admin', context='dashboard.)
    config.include('pyramid_handlers')
    
    config.add_handler("default", "/", action="home",
                       handler="dashboard.views.handlers.LoggedInHandler")
    config.add_handler("users", "/users/{action}*id",
                       handler="dashboard.views.handlers.UserAccountHandler", traverse='/users')
    
    config.scan()
    return config.make_wsgi_app()
