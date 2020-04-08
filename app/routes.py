from aiohttp import web
from app.api import events


routes = [web.get('/index', events.handlers.index)]