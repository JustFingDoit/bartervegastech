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
    config.include('pyramid_handlers')
    config.add_handler("default", "/", action="home",
                       handler="bartervegastech.views.handlers.PageHandler")
    config.add_handler("user", "/user/{action}*id",
                       handler="bartervegastech.views.handlers.UserAccountHandler", traverse='/user')
    config.add_handler("pages", "/{action}*id", 
                        handler="bartervegastech.views.handlers.PageHandler")
    config.scan()
    return config.make_wsgi_app()
