from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

import configs
from app import api, main
from app.services import databases
from app.temaplting import templates

__version__ = '0.0.1'


def create_app() -> FastAPI:
    app = FastAPI(
        version=__version__,
        on_startup=[
            databases.connect,
        ],
        on_shutdown=[
            databases.disconnect,
        ],
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_methods=['*'],
        allow_headers=['*'],
        allow_credentials=True,
    )

    app.mount(
        path=configs.STATIC_URL,
        app=StaticFiles(directory=configs.STATIC_DIR),
        name='static',
    )

    app.include_router(api.router)
    app.include_router(main.router)

    templates.add_global('__version__', __version__)

    return app
