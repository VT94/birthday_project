from aiohttp import web

from .api import persons

routes = [
    web.route(path='/person', method='GET', handler=persons.show_person),
    web.route(path='/person', method='POST', handler=persons.add_person),
    web.route(path='/person/{id}', method='DELETE', handler=persons.del_person),
]
