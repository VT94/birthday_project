from app.api.schema import schema_add


class Handler:
    async def hand(self, request, SQL):
        pool = request.app.db
        connection = await pool.acquire()
        result = await self.person_show(connection, SQL)
        await pool.release(connection)
        return result

    async def person_show(self, connection, SQL):
        result = await connection.fetch(SQL)
        return {record['name']: str(record['birthday']) for record in result}

    async def event(self,connection, SQL, payload):
        await connection.execute(SQL)


app_handler = Handler()
