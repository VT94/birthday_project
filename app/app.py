from typing import Optional

import asyncpg
from aiohttp import web
from aiohttp.web import Application
from asyncpg.pool import Pool

import settings
from . import middlewares, routes


class App(Application):
    db: Optional[Pool] = None


async def run_db(app: App) -> None:
    app.db = await asyncpg.create_pool(dsn=settings.dsn)


async def close_db(app: App) -> None:
    await app.db.close()


def create_app() -> App:
    app = web.Application(middlewares=[middlewares.error_middleware])
    app.add_routes(routes.routes)
    app.on_startup.append(run_db)
    app.on_cleanup.append(close_db)

    return app
