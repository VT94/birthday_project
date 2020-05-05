from datetime import datetime
from asyncpg import Connection
from app.api import schema_show


async def show_all(connection: Connection) -> dict:
    result = await connection.fetch('''SELECT id, name, birthday FROM person''')
    data = schema_show.dump(result, many=True)
    return data


async def show_id_person(connection: Connection, id_: int) -> dict:
    result = await connection.fetch('''SELECT id, name, birthday FROM person WHERE id=$1''', id_)
    data = schema_show.dump(result, many=True)
    return data


async def birthday_date(connection: Connection, date: datetime) -> dict:
    result = await connection.fetch('''SELECT id, name, birthday FROM person WHERE birthday=$1''', date)
    data = schema_show.dump(result, many=True)
    return data
