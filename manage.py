from aiohttp import web
from app import routes, db_conn

app = web.Application()
app.add_routes(routes.routes)
app.on_startup.append(db_conn.run_db)
app.on_cleanup.append(db_conn.close_db)
if __name__ == '__main__':
    web.run_app(app)
