from datetime import datetime
from typing import Optional, List

from asyncpg import Connection, Record


async def show_query(connection: Connection,
                     id: Optional[int] = None, birthday: Optional[datetime] = None) -> List[Record]:
    return await connection.fetch('''
        SELECT id, name, birthday 
        FROM person 
        WHERE 
            ($1::integer is NULL or $1=id) and 
            ($2::date is NULL or $2=birthday);
        ''', id, birthday)


async def create_query(connection: Connection, name: str, birthday: datetime) -> Record:
    return await connection.fetchrow('''
        INSERT INTO person
            (name, birthday) 
        VALUES
            ($1, $2) 
        returning id;
        ''', name, birthday)


async def del_query(connection: Connection, name: str) -> Record:
    return await connection.fetchrow('''
        DELETE FROM person WHERE name=$1 returning id;
        ''', name)
