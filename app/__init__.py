from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import api

__version__ = '0.0.1'


def create_app() -> FastAPI:
    app = FastAPI(
        version=__version__,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_methods=['*'],
        allow_headers=['*'],
        allow_credentials=True,
    )

    app.include_router(api.router)

    return app
