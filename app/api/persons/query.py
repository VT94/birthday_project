from datetime import datetime
from asyncpg import Connection


async def show_person_SQL(connection: Connection, id: int = None, birthday: datetime = None) -> list:
    result = await connection.fetch('''SELECT * FROM person WHERE 
                                       ($1::integer is NULL or $1=id) and ($2::date is NULL or $2=birthday)''', id, birthday)
    return result


