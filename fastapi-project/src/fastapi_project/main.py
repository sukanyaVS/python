from fastapi import FastAPI
from fastapi_project.routers import users, books
from fastapi_project.routers import books, departments, users

app = FastAPI()

app.include_router(users.router)
app.include_router(books.router)
app.include_router(departments.router)