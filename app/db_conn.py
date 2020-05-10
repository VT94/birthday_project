import asyncpg
import settings
from aiohttp.web import Application


async def run_db(app: Application) -> None:
    pool = await asyncpg.create_pool(dsn=settings.dsn)
    app.db = pool


async def close_db(app: Application) -> None:
    app.db.close()
    await app.db.wait_closed()
