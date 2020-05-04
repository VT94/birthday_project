from datetime import datetime
from asyncpg import Connection


async def add_person_SQL(connection: Connection, name: str, birthday: datetime) -> dict:
    id_ = await connection.fetchrow('''INSERT INTO person(name, birthday) VALUES($1, $2) returning id''', name,
                                    birthday)
    return dict(id_)


async def del_person_SQL(connection: Connection, name: str) -> dict:
    id_ = await connection.fetchrow('''DELETE FROM person WHERE name=$1 returning id''', name)
    return dict(id_)
