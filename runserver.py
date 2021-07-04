import uvicorn

from app import create_app
from configs import config

app = create_app()

if __name__ == '__main__':
    uvicorn.run(
        app='runserver:app',
        host=config.HOST,
        port=config.PORT,
        reload=config.RELOAD,
    )
