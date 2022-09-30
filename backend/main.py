from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


async def homepage(request):
    return JSONResponse({'hello': 'world'})

async def school(request):
    return JSONResponse({'lesson': 'software engineering'})


app = Starlette(debug=True, routes=[
    Route('/hello', homepage),
    Route('/lesson', school),
])