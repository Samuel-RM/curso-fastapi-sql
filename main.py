from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from jwt_manager import create_token 
from config.database import  engine, Base
from middleware.error_handler import  ErrorHandler
from routers.movie import movie_router
from routers.users import user_router

app = FastAPI()
app.title = "Mi aplicación con  FastAPI"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(user_router)


Base.metadata.create_all(bind=engine)


@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello world</h1>')

