from json.decoder import JSONDecodeError

from aiohttp import web
from marshmallow.exceptions import ValidationError

from app.exception import BadRequestError
from . import schema
from .query import show_query, create_query, del_query


async def show_person(request) -> web.Response:
    try:
        query = schema.FilterPersons().load(request.query)
    except ValidationError:
        raise BadRequestError
    pool = request.app.db
    async with pool.acquire() as conn:
        data = await show_query(conn, **query)
        out_data = schema.Person().dump(data, many=True)
    return web.json_response(data=out_data)


async def add_person(request) -> web.Response:
    try:
        payload = await request.json()
        data = schema.Person(exclude=('id',)).load(payload)
    except (ValidationError, JSONDecodeError):
        raise BadRequestError
    pool = request.app.db
    async with pool.acquire() as conn:
        res = await create_query(conn, **data)
        out_data = schema.Person().dump(res)
    return web.json_response(data=out_data)


async def del_person(request) -> web.Response:
    try:
        payload = await request.json()
        data = schema.Person(only=('name',)).load(payload)  # todo  delete by id
    except (ValidationError, JSONDecodeError):
        raise BadRequestError
    pool = request.app.db
    async with pool.acquire() as conn:
        res = await del_query(conn, name=data['name'])
        out_data = schema.Person().dump(res)
    return web.json_response(data=out_data)
