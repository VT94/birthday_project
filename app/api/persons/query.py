from datetime import datetime
from asyncpg import Connection


async def show_all(connection: Connection) -> dict:
    result = await connection.fetch('''SELECT name, birthday FROM person''')
    return {record['name']: str(record['birthday']) for record in result}


async def show_id_person(connection: Connection, id_: int) -> dict:
    result = await connection.fetch('''SELECT name, birthday FROM person WHERE id=$1''', id_)
    return {record['name']: str(record['birthday']) for record in result}


async def birthday_date(connection: Connection, date: datetime) -> dict:
    result = await connection.fetch('''SELECT name, birthday FROM person WHERE birthday=$1''', date)
    return {record['name']: str(record['birthday']) for record in result}
