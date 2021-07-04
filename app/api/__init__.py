from fastapi import APIRouter

from . import hello_word

router = APIRouter(prefix='/api')

router.include_router(
    router=hello_word.router,
    tags=['hello_word'],
)
