from fastapi import FastAPI
from app.database.database import engine, Base
from app.routers import user

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI con MySQL")

app.include_router(user.router)

@app.get("/")
def read_root():
    return {"message": "API conectada a MySQL correctamente"}