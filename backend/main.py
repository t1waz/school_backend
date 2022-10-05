from datetime import datetime
from starlette.applications import Starlette
from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request
from starlette.responses import JSONResponse, RedirectResponse
from starlette.routing import Route

import constants


class HealthCheckEndpoint(HTTPEndpoint):
    """
    Just to see if backend is up.
    """

    async def get(self, request: Request, *args, **kwargs) -> JSONResponse:
        return JSONResponse({'status': 'ok'})


async def homepage(request):
    return JSONResponse({'hello': 'world'})


async def julian_endpoint(request):
    return JSONResponse({'date': str(datetime.now())})


async def school(request):
    return JSONResponse({'lesson': 'software engineering'})


async def tomasz(request):
    return RedirectResponse({'https://www.youtube.com/watch?v=AFhZxua-2P8': 303})


async def google(request):
    return JSONResponse({'Here is google': 'something went wrong'})


async def mayonnaise(request):
    return RedirectResponse('https://www.youtube.com/embed/9K2Y-rfUy_4?autoplay=1&mute=1&controls=0', 303)


app = Starlette(debug=True, routes=[
    Route('/hello', homepage),
    Route('/julian', julian_endpoint),
    Route('/lesson', school),
    Route('/google', google),
    Route('/mayonnaise', mayonnaise),
    Route(constants.HEALTH_CHECK_ENDPOINT, HealthCheckEndpoint),
])
