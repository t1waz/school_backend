from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from datetime import datetime


async def homepage(request):
    return JSONResponse({'hello': 'world'})

async def julian_endpoint(request):
    date = str(datetime.now())
    return JSONResponse({'date': date})


app = Starlette(debug=True, routes=[
    Route('/hello', homepage),
    Route('/julian', julian_endpoint),
])