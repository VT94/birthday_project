async def show_person(request):
    connection = request.app.db
    pass


async def show_id(request):
    connection = request.app.db
    request_id = request.match_info.get('id')
    pass


async def today(request):
    pass
