from aiohttp import web
from app.api import events
from app.api import persons

routes = [web.get('/show_person', persons.show_person),
          web.get('/show_person/id/{id}', persons.show_person), web.get('/show_person/birthday/{birthday}', persons.show_person),
          web.post('/add_person', events.add_person), web.delete('/del_person', events.del_person)]
