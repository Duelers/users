from aiohttp import web
from models import users


async def add_user(request):
    async with request.app['db'].acquire() as conn:
        data = await request.json()
        password = data["password"]
        username = data["username"]

        await conn.execute(users.insert().values(username=username.lower(), password=password))

        return web.json_response(data={}, status=201)
