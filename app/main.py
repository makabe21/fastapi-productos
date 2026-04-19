from fastapi import FastAPI
from app.database.database import engine, Base
from app.routers import producto_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI con MySQL")

app.include_router(producto_router.router)