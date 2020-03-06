from aiohttp import web
from models import users


async def get_user(request):
    async with request.app['db'].acquire() as conn:
        username = request.match_info['name']

        cursor = await conn.execute(users.select().where(users.c.username == username.lower()))
        result = await cursor.fetchone()

        if result:
            return web.json_response(data={"username": result.username})
        else:
            return web.json_response(data={"error": "not found"}, status=404)
