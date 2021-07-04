from ormar import NoMatch

from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse

from app.models import URL
from app.temaplting import templates
from app.services import link_counter

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
        url_obj = await URL.objects.get(URL.origin_url == url)
    except NoMatch:
        url_obj = await URL(origin_url=url, url_alias=URL.create_alias(url)).save()

    counter = await link_counter.get_counter(url_obj.url_alias)

    context = {
        'request': request,
        'counter': counter,
        'origin_url': url_obj.origin_url,
        'short_url': url_obj.get_short_url(str(request.base_url)),
    }
    return templates.TemplateResponse('index.html', context)