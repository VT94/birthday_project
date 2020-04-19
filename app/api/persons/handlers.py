from aiohttp import web
from app.api.handler import app_handler
import datetime as dt


async def show_person(request) -> 'json':
    SQL = 'SELECT name, birthday FROM person'
    out_data = await app_handler.hand_show(request, SQL)
    return web.json_response(data=out_data)


async def show_id(request) -> 'json':
    request_id = request.match_info.get('id')
    SQL = 'SELECT name, birthday FROM person WHERE id = {}'.format(request_id)
    out_data = await app_handler.hand_show(request, SQL)
    return web.json_response(data=out_data)


async def today(request) -> 'json':
    today_month = dt.datetime.today().date().month
    today_day = dt.datetime.today().date().day
    SQL = 'SELECT name, birthday FROM person WHERE extract(month from birthday) = {} and ' \
          'extract(day from birthday) = {}'.format(today_month, today_day)
    out_data = await app_handler.hand(request, SQL)
    return web.json_response(data=out_data)
