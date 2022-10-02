from starlette.applications import Starlette
from starlette.responses import JSONResponse, Response
from starlette.routing import Route


async def homepage(request):
    return JSONResponse({'hello': 'world'})

async def school(request):
    return JSONResponse({'lesson': 'software engineering'})

async def shanties(request):
    f = open('./shanties.txt', 'r')
    return Response(f.read(), media_type='text/plain')

app = Starlette(debug=True, routes=[
    Route('/hello', homepage),
    Route('/lesson', school),
    Route('/shanties', shanties)
])