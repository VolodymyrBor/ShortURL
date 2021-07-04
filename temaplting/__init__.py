from functools import lru_cache

from configs import TEMPLATE_DIR
from app.shared.jinja import JinjaTemplates

from . import filters


@lru_cache()
def get_templates() -> JinjaTemplates:
    templates_ = JinjaTemplates(str(TEMPLATE_DIR))
    templates_.include_register(filters.register)
    return templates_


templates = get_templates()
