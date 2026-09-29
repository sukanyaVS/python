from fastapi import FastAPI
from fastapi_project.routers import users, books

app = FastAPI()

app.include_router(users.router)
app.include_router(books.router)