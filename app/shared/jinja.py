from typing import Callable, Optional, Any

from fastapi.templating import Jinja2Templates


class Register:
    """Register for jinja2 tags"""

    def __init__(self):
        self.filters: dict[str, Callable] = {}

    def filter(self, name: Optional[str] = None, func: Optional[Callable] = None) -> Callable:

        def wrapper(func_: Callable) -> Callable:
            self._add_filter(func_, name=name)
            return func_

        if func:
            self._add_filter(func, name=name)
            return func
        else:
            return wrapper

    def _add_filter(self, func: Callable, name: Optional[str] = None):
        self.filters[name or func.__name__] = func


class JinjaTemplates(Jinja2Templates):

    def __init__(self, directory: str):
        super().__init__(directory=directory)

    def include_register(self, register: Register):
        """Add register to jinja environment"""
        self.env.filters.update(register.filters)

    def add_global(self, name: str, value: Any):
        """Add global to jinja environment"""
        self.env.globals[name] = value
