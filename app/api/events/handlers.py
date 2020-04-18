from aiohttp import web
from app.api.handler import app_handler


async def hello(request):
    return web.json_response(data='Hello')


async def add_person(request):
    payload = await request.json()
    SQL = '''
                INSERT INTO person(name, birthday) VALUES($1, $2)
            ''', payload['name'], payload['birthday']
    app_handler.hand(request, SQL, payload=payload, event='Add')


async def del_person(request):
    pass
