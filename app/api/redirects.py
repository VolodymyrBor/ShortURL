from fastapi.responses import RedirectResponse
from fastapi import APIRouter, HTTPException, status

from ormar import NoMatch

from app.models import URL
from app.services import link_counter

router = APIRouter()


@router.get('/{url_alias}')
async def redirect(url_alias: str) -> RedirectResponse:
    """Get link alias and redirect to original url"""
    try:
        url = await URL.objects.get(URL.url_alias == url_alias)
    except NoMatch:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='URL not found')
    await link_counter.inc_link_counter(url_alias)
    return RedirectResponse(url.origin_url)
