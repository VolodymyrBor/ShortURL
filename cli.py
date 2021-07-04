import sqlalchemy
from typer import Typer

from configs import config
from app.models import metadata

app = Typer()

engine = sqlalchemy.create_engine(config.DB.url)


@app.command('create-tables')
def create_tables():
    metadata.create_all(engine)


@app.command('drop-tables')
def create_tables():
    metadata.drop_all(engine)


if __name__ == '__main__':
    app()
