from datetime import datetime
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


async def homepage(request):
    return JSONResponse({'hello': 'world'})

async def julian_endpoint(request):
    return JSONResponse({'date': str(datetime.now())})


app = Starlette(debug=True, routes=[
    Route('/hello', homepage),
    Route('/julian', julian_endpoint),
])