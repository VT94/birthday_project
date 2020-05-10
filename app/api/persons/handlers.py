from aiohttp import web
from .query import show_person_SQL
from app.exception import BadRequestError
from app.api import schema_show
from marshmallow.exceptions import ValidationError


async def show_person(request) -> web.Response:
    try:
        query = schema_show.load(request.match_info)
    except ValidationError:
        raise BadRequestError
    pool = request.app.db
    async with pool.acquire() as conn:
        data = await show_person_SQL(conn, **query)
        out_data = schema_show.dump(data, many=True)
    return web.json_response(data=out_data)
