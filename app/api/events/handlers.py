from aiohttp import web
from app.api.schema import schema_add, schema_del
from app.api.events.query import add_person_SQL, del_person_SQL
from app.exception import BadRequestError
from marshmallow.exceptions import ValidationError
from json.decoder import JSONDecodeError


async def add_person(request) -> web.Response:
    try:
        payload = await request.json()
        data = schema_add.load(payload)
    except (ValidationError, JSONDecodeError):
        raise BadRequestError
    pool = request.app.db
    async with pool.acquire() as conn:
        id_ = await add_person_SQL(conn, **data)
    return web.json_response(data=id_)


async def del_person(request) -> web.Response:
    try:
        payload = await request.json()
        data = schema_del.load(payload)
    except (ValidationError, JSONDecodeError):
        raise BadRequestError
    pool = request.app.db
    async with pool.acquire() as conn:
        id_ = await del_person_SQL(conn, name=data['name'])
    return web.json_response(data=id_)