from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse

from app.temaplting import templates


router = APIRouter()

@router.get('/', tags=['index'])
def index(request: Request) -> HTMLResponse:
    context = {
        'request': request,
    }
    return templates.TemplateResponse('index.html', context)


@router.post('/', tags=['index'])
def index(request: Request, url: str = Form(...)) -> HTMLResponse:
    context = {
        'request': request,
        'url': url,
    }
    return templates.TemplateResponse('index.html', context)