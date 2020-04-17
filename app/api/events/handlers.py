from aiohttp import web


async def index(request):
    return web.Response(text='Hello')


async def add_person(request):
    pass


async def del_person(request):
    pass
