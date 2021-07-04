from pathlib import Path
from functools import lru_cache

import yaml

from configs.models import Config


CONFIG_DIR = Path(__file__).parent

CONFIG_FILE = CONFIG_DIR / 'config.yaml'
BASE_CONFIG_FILE = CONFIG_DIR / 'base.yaml'

ROOT_DIR = CONFIG_DIR.parent
APP_DIR = ROOT_DIR / 'app'
TEMPLATE_DIR = APP_DIR / 'templates'
STATIC_DIR = APP_DIR / 'static'

STATIC_URL = '/static'


@lru_cache
def get_config() -> Config:
    """Create application config from configs/base.yaml and configs/config.yaml"""

    conf = yaml.safe_load(BASE_CONFIG_FILE.read_text())

    if CONFIG_FILE.exists():
        extra_conf = yaml.safe_load(CONFIG_FILE.read_text())
        conf.update(extra_conf)

    return Config(**conf)


config = get_config()
