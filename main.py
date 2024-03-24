from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from db import models
from db.database import engine
from routers import user, image
from auth import authentication

app = FastAPI()
app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(image.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}

models.Base.metadata.create_all(engine)

app.mount('/images_store', StaticFiles(directory="images_store"), name="images")
