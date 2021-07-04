import hashlib

import ormar
import sqlalchemy

from configs import config
from app.services.databases import database, metadata


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class URL(ormar.Model):

    class Meta(BaseMeta):
        tablename = 'urls'

    pk: int = ormar.Integer(primary_key=True, autoincrement=True)
    full_url: str = ormar.String(max_length=512, index=True, unique=True)
    url_alias: str = ormar.String(max_length=128, unique=True)

    def get_short_url(self, host: str) -> str:
        return f'{host}api/{self.url_alias}'

    @staticmethod
    def create_alias(url: str) -> str:
        return hashlib.md5(url.encode('utf-8')).hexdigest()


if __name__ == '__main__':
    engine = sqlalchemy.create_engine(config.DB.url)
    metadata.drop_all(engine)
    metadata.create_all(engine)