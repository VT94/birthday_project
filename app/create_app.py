from aiohttp import web
import asyncpg
import settings
from app import routes


async def init_app():
    app = web.Application()
    app.db = await run_db()
    app.add_routes(routes.routes)
    return app


async def run_db():
    poll = await asyncpg.create_pool(dsn='postgres://postgres:{}@localhost/my_database'.format(settings.PASSWORD))
    return poll
