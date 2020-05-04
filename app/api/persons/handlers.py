from aiohttp import web
from .query import show_all, show_id_person, birthday_date
from datetime import datetime as dt
from app.exception import BadRequestError


async def show_person(request) -> web.Response:
    pool = request.app.db
    async with pool.acquire() as conn:
        out_data = await show_all(conn)
    return web.json_response(data=out_data)


async def show_id(request) -> web.Response:
    try:
        request_id = int(request.match_info.get('id'))
        pool = request.app.db
        async with pool.acquire() as conn:
            out_data = await show_id_person(conn, id_=request_id)
        return web.json_response(data=out_data)
    except ValueError as err:
        raise BadRequestError(err)


async def date(request) -> web.Response:
    try:
        date = dt.strptime(request.match_info.get('date'), '%Y-%m-%d')
        pool = request.app.db
        async with pool.acquire() as conn:
            out_data = await birthday_date(conn, date=date)
        return web.json_response(data=out_data)
    except ValueError as err:
        raise BadRequestError(err)
