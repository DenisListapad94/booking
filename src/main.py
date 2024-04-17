from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from src.auth.routers.base import router as auth_router
from src.book_app.routers.base import router as book_router

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(auth_router)
app.include_router(book_router)


@app.get("/get_template", response_class=HTMLResponse)
def get_html_template(request: Request):
    users = [
        {"username": "Peter", "age": 24},
        {"username": "Max", "age": 21},
        {"username": "Ann", "age": 18},
        {"username": "Volodya", "age": 30},
        {"username": "Elena", "age": 32},
    ]

    return templates.TemplateResponse(
        request=request,
        name="item.html",
        context={
            "data": 2132.2,
            "users": users
        }
    )
