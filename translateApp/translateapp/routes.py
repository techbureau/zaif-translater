def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_static_view('html', 'html', cache_max_age=3600)
    config.add_route('register', '/register')
    config.add_route('edit', '/edit')
    config.add_route('search', '/search')
    config.add_route('get_csv', '/get_csv')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
