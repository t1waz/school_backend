from starlette.applications import Starlette
from starlette.responses import JSONResponse, Response
from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request
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


async def school(request):
    return JSONResponse({'lesson': 'software engineering'})

async def shanties(request):
    f = open('./shanties.txt', 'r')
    return Response(f.read(), media_type='text/plain')

async def google(request):
    return JSONResponse({'Here is google': 'something went wrong'})


app = Starlette(debug=True, routes=[
    Route('/hello', homepage),
    Route('/lesson', school),
    Route('/shanties', shanties)
    Route('/google', google),
    Route(constants.HEALTH_CHECK_ENDPOINT, HealthCheckEndpoint),
])