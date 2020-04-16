from aiohttp import web
from settings import config
from db import close_pg, init_pg
from routes import setup_routes
import logging

stdio_handler = logging.StreamHandler()
stdio_handler.setLevel(logging.INFO)
_logger = logging.getLogger('aiohttp.access')
_logger.addHandler(stdio_handler)
_logger.setLevel(logging.DEBUG)

app = web.Application(logger=_logger)
app['config'] = config
app.on_startup.append(init_pg)
app.on_cleanup.append(close_pg)
setup_routes(app)
web.run_app(app)
