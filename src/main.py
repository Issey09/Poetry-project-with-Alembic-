from fastapi import  FastAPI

from src.database.database import Base, engine
from src.routers.router import router
Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(router)