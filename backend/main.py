from datetime import datetime, date
from json import detect_encoding
from starlette.applications import Starlette
from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request
from starlette.responses import JSONResponse
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

async def oliwier(request):
    return JSONResponse({'Oliwier is': "Fisherman"})

async def school(request):
    return JSONResponse({'lesson': 'software engineering'})


async def google(request):
    return JSONResponse({'Here is google': 'something went wrong'})


app = Starlette(debug=True, routes=[
    Route('/hello', homepage),
    Route('/julian', julian_endpoint),
    Route('/lesson', school),
    Route('/google', google),
    Route('/oliwier', oliwier),
    Route(constants.HEALTH_CHECK_ENDPOINT, HealthCheckEndpoint),
])