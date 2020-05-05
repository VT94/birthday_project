from aiohttp import web
from app.api.persons.query import show_all, show_id_person, birthday_date
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
        if 'id' in query:
            out_data = await show_id_person(conn, id_=query['id'])
            return web.json_response(data=out_data)
        elif 'birthday' in query:
            out_data = await birthday_date(conn, date=query['birthday'])
            return web.json_response(data=out_data)
        out_data = await show_all(conn)
    return web.json_response(data=out_data)
