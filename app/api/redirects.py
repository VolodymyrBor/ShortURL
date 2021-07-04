from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from app.models import URL

router = APIRouter()


@router.get('/{url_alias}')
async def redirect(url_alias: str) -> RedirectResponse:
    url = await URL.objects.get(URL.url_alias == url_alias)
    return RedirectResponse(url.full_url)
