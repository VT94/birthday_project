from aiohttp import web
from app.api import events
from app.api import persons

routes = [web.get('/index', events.handlers.index), web.get('/show_person', persons.handlers.show_person),
          web.get('/show_person/{id}', persons.handlers.show_id)]
