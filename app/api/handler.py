class Handler:
    async def hand_show(self, request, SQL: str) -> dict:
        pool = await self.pool(request)
        result = await self.person_show(pool[1], SQL)
        await pool[0].release(pool[1])
        return result

    async def person_show(self, connection, SQL: str) -> dict:
        result = await connection.fetch(SQL)
        return {record['name']: str(record['birthday']) for record in result}

    async def query(self, request, SQL: str, *args) -> None:
        pool = await self.pool(request)
        await pool[1].execute(SQL, *args)
        await pool[0].release(pool[1])

    async def pool(self, request) -> list:
        pool = request.app.db
        connection = await pool.acquire()
        return [pool, connection]


app_handler = Handler()
