from aiohttp import web
from app.api import events
from app.api import persons

routes = [web.get('/', events.hello), web.get('/show_person', persons.show_person),
          web.get('/show_person/{id}', persons.show_id), web.get('/today', persons.today]
