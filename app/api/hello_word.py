from fastapi import APIRouter


router = APIRouter()


@router.get('/')
def hello_word() -> str:
    return 'Hello Word'
