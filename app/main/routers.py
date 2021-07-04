from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from app.temaplting import templates


router = APIRouter()

@router.get('/', tags=['index'])
def index(request: Request) -> HTMLResponse:
    context = {
        'request': request,
    }
    return templates.TemplateResponse('index.html', context)