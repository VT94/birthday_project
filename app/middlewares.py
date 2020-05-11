from aiohttp import web

from app.exception import BaseApiException


@web.middleware
async def error_middleware(request, handler):
    try:
        return await handler(request)
    except web.HTTPException as err:
        return web.json_response({'error': f'Code: {err.status_code}, message: {err.reason}'})
    except BaseApiException as err:
        return web.json_response({'error': f' {err}'})
