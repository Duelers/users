from views import add_user, get_user, validate_password


def setup_routes(app):
    app.router.add_get('/v1/users/{name}/', get_user)
    app.router.add_post('/v1/users/', add_user)
    app.router.add_post('/v1/users/{name}/validate/', validate_password)
