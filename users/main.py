from aiohttp import web
from settings import config
from db import close_pg, init_pg
from routes import setup_routes

app = web.Application()
app['config'] = config
app.on_startup.append(init_pg)
app.on_cleanup.append(close_pg)
setup_routes(app)
web.run_app(app)
