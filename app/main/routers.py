from ormar import NoMatch

from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse

from app.models import URL
from app.temaplting import templates


router = APIRouter()


@router.get('/', tags=['index'])
async def index(request: Request) -> HTMLResponse:
    context = {
        'request': request,
    }
    return templates.TemplateResponse('index.html', context)


@router.post('/', tags=['index'])
async def index(request: Request, url: str = Form(...)) -> HTMLResponse:

    try:
        url_obj = await URL.objects.get(URL.full_url == url)
    except NoMatch:
        url_obj = await URL(full_url=url, url_alias=URL.create_alias(url)).save()

    context = {
        'request': request,
        'full_url': url_obj.full_url,
        'short_url': url_obj.get_short_url(str(request.base_url)),
    }
    return templates.TemplateResponse('index.html', context)