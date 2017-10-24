from pyramid.config import Configurator


def main(global_config, **settings):
    """ Эта функция возвращает приложение Pyramid WSGI.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()
