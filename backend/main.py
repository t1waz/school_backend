from datetime import datetime
from starlette.applications import Starlette
from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request
from starlette.responses import JSONResponse, RedirectResponse, PlainTextResponse
from starlette.routing import Route

import constants
import base64


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

async def google(request):
    return JSONResponse({'Here is google': 'something went wrong'})

async def piotrek_endpoint(request):
    return JSONResponse({'My late counter ':'∞'})

async def mayonnaise(request):
    return RedirectResponse('https://www.youtube.com/embed/9K2Y-rfUy_4?autoplay=1&mute=1&controls=0', 303)


async def capybara_endpoint(request):
    return PlainTextResponse(base64.b64decode("""
    4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qOk4qOE4qKY4qOS4qOA4qOA4qOA4qOA4qCA4qCA4qCAICAgICAg4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qKA4qOe4qOG4qKA4qOg4qK24qGE4qCA4qCAICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIArioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDio73io7/io5vioJviopvio7/io7/iob/ioJ/ioILioIAgICAgICAg4qCA4qKA4qOA4qGk4qCk4qCW4qCS4qCL4qCJ4qOJ4qCJ4qC54qKr4qC+4qOE4qGA4qCAICAgICAgICAgCuKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKjgOKjgOKjgOKjgOKhgOKggOKjpOKjvuKjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjt+Kjv+KhhuKggCAgICAgICDioqDioY/iorDiobTioIDioIDioIDioInioJnioJ/ioIPioIDioIDioIDioIjioJnioKbio4TioYDiooDio4Dio6DioaTioKTioLbioJLioJLior/ioIvioIjioIDio5LioZLioLLioKTio4TioYDioIDioIDioIDioIDioIDioIAgICAK4qCA4qCA4qCA4qCA4qCA4qCA4qOA4qOk4qO24qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qG/4qCB4qCAICAgICAgIOKiuOKggOKiuOKggeKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKgiOKgieKggOKgtOKgguKjgOKggOKggOKjtOKhhOKgieKit+KhhOKgmuKggOKipOKjkuKgpuKgieKgs+KjhOKhgOKggOKggOKggCAgIArioIDioIDioIDiooDio7Tio77io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/ioYfioIDioIDioIDioIDioIDioIAgICAgICAg4qC44qGE4qC84qCm4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qOE4qGC4qCg4qOA4qCQ4qCN4qCC4qCZ4qOG4qCA4qCAICAgCuKggOKggOKjoOKjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Khh+KggOKggOKggOKggOKggOKggCAgICAgICAg4qCA4qCZ4qCm4qKE4qOA4qOA4qOA4qOA4qGA4qCA4qK34qCA4qKm4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCw4qGH4qCg4qOA4qCx4qCY4qOn4qCAICAK4qCA4qCA4qC74qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qCf4qCc4qCA4qCA4qCA4qCA4qCA4qCA4qCAICAgICAgICDioIDioIDioIDioIDioIDioIDioIDioIjioIniorfio6fioYTiorzioIDiooDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIjioIDioYjioIDiooTiorjioYQgIArioIDioIDioIDior/io7/io7/io7/io7/ioL/ioL/io7/io7/iob/ior/io7/io7/ioIjio7/io7/io7/ioY/io6DiobTioIDioIDioIDioIDioIDioIDioIAgICAgICAgICAgICAgICAgICAgICDioJnio7/ioYDioIPioJjioILioLLioYDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioJnioIDioYjiopjioYcK4qCA4qCA4qOg4qO/4qO/4qO/4qG/4qKB4qO04qO24qOE4qCA4qCA4qCJ4qCJ4qCJ4qCA4qK74qO/4qG/4qKw4qO/4qGH4qCA4qCA4qCA4qCA4qCA4qCA4qCAICAgICAgICAgIOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKgiOKiq+KhkeKgo+KgsOKggOKigeKigOKhgOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggeKjuOKggQrioIDioIDior/io7/ioJ/ioIvioIDioIjioJvio7/io7/ioIDioIDioIDioIDioIDioIDioLjio7/ioYfiorjio7/ioYfioIDioIDioIDioIDioIDioIDioIAgICAgICDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIAgICDioJnio6/ioILioYDioqjioIDioIPioIDioIDioIDioIDioIDioIDioIDioIDioIDiooDioYbio77ioYTioIDioIDioIDioIDio4DioJDioIHiobTioIHioIAK4qCA4qCA4qK44qO/4qCA4qCA4qCA4qCA4qCA4qCY4qC/4qCG4qCA4qCA4qCA4qCA4qCA4qCA4qO/4qGH4qCA4qC/4qCH4qCA4qCA4qCA4qCA4qCA4qCA4qCAICAgICAg4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCAICAg4qCI4qOn4qGI4qGA4qKg4qOn4qOk4qOA4qOA4qGA4qKA4qGA4qCA4qCA4qKA4qO84qOA4qCJ4qGf4qCA4qKA4qGA4qCY4qKT4qOk4qGe4qCB4qCA4qCACuKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggCAgICAgIOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggCAgICAgICAgICAgICAgICAgICAgICDiorrioYHiooHio7jioY/ioIDioIDioIDioIDioIHioIDioInioInioIHioLnioZ/ioqLiorHioIDiorjio7fioLbioLvioYfioIDioIDioIDioIAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIAgIOKiiOKhj+KgiOKhn+Khh+KggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKgkeKihOKggeKggOKgu+Kjp+KggOKggOKjueKggeKggOKggOKggAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggCAg4qOA4qOA4qGk4qCa4qCD4qOw4qOl4qCH4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qKA4qO+4qC84qKZ4qG34qG74qCA4qG84qCB4qCA4qCA4qCA4qCACiAgICAgICAgICAgICAgICAgIPCdlY7wnZWW8J2VnfCdlZTwnZWg8J2VnvCdlZYg8J2VpfCdlaAg8J2VpfCdlZnwnZWWIPCdlaTwnZWW8J2VlPCdlaPwnZWW8J2VpSDwnZWU8J2VkvCdlaHwnZWq8J2Vk/CdlZLwnZWj8J2VkiDwnZWW8J2Vn/CdlZXwnZWh8J2VoPCdlZrwnZWf8J2VpSDioIjioJ/ioL/iob/ioJXioIrioInioIDioIDioIDioIDioIDioIDioIDioIDio6Dio7Tio7bio77ioInio7nio7fio5/io5rio4HiobzioIHioIDioIDioIDioIDioIAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIAgIOKgieKgmeKgi+KggeKggOKgieKgieKgieKgieKggeKggOKggOKggOKggOKggOKggOKggAoK
    """))

async def tomasz(request):
    return JSONResponse({'concrete workers from england, you have greetings from poland, co..cooo.cooo..concrete!': "https://www.youtube.com/embed/9K2Y-rfUy_4?autoplay=1&mute=1&controls=0"})

async def drunkensailor(request):
	return JSONResponse({'with the drunken sailor':'early in the morning'})

app = Starlette(debug=True, routes=[
    Route('/hello', homepage),
    Route('/capybara', capybara_endpoint),
    Route('/julian', julian_endpoint),
    Route('/lesson', school),
    Route('/google', google),
    Route('/piotrek', piotrek_endpoint),
    Route('/mayonnaise', mayonnaise),
    Route('/tomasz', tomasz),
    Route('/whatdowedo', drunkensailor)
    Route(constants.HEALTH_CHECK_ENDPOINT, HealthCheckEndpoint),
])
