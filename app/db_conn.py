import asyncpg
import settings


async def run_db(app):
    pool = await asyncpg.create_pool(dsn=settings.dsn)
    app.db = pool


async def close_db(app):
    app.db.close()
    await app.db.wait_closed()
