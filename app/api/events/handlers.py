from aiohttp import web
from app.api.handler import app_handler
from app.api.schema import schema_add, schema_del
from app.api.events.query import SQL


async def hello(request) -> 'json':
    return web.json_response(data='Hello')


async def add_person(request) -> None:
    try:
        payload = await request.json()
        data = await schema_add.validate_in(payload)
        await app_handler.query(request, SQL['Add_person'], data['name'], data['birthday'])
    except Exception as error:
        print(error)


async def del_person(request) -> None:
    try:
        payload = await request.json()
        data = await schema_del.validate_in(payload)
        await app_handler.query(request, SQL['Del_person'], data['name'])
    except Exception as error:
        print(error)
