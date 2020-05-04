from aiohttp import web
from app.exception import BadRequestError


@web.middleware
async def error_middleware(request, handler):
    try:
        response = await handler(request)
        return response
    except web.HTTPException as err:
        return web.json_response({'error': f'Code: {err.status_code}, message: {err.reason}'})
    except BadRequestError as err:
        return web.json_response({'error': f'Code: {err.status_code}, message: {err.message}'})