import datetime as dt

from app.shared.jinja import Register

register = Register()


@register.filter('date')
def date_filter(value: dt.datetime, fmt: str = '%Y-%m-%d') -> str:
    return value.strftime(fmt)
