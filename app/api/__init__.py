from fastapi import APIRouter

from . import redirects

router = APIRouter(prefix='/api')

router.include_router(
    router=redirects.router,
    tags=['hello_word'],
)
