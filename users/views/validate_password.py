from aiohttp import web
from passlib.hash import pbkdf2_sha256
from models import users


async def validate_password(request):
    async with request.app['db'].acquire() as conn:
        username = request.match_info['name']
        data = await request.json()
        password = data["password"]

        cursor = await conn.execute(users.select().where(users.c.username == username.lower()))
        result = await cursor.fetchone()

        if result:
            password_hash = result.password
            if pbkdf2_sha256.verify(password, password_hash):
                return web.json_response(data={}, status=204)

        return web.json_response(data={}, status=403)
