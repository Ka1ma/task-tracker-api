from fastapi import FastAPI
from app.routes import auth_routes, task_routes

app = FastAPI(
    title="Assignment Task Tracker API",
    description="Backend Task Management API with FastAPI, MongoDB & JWT",
    version="1.0.0"
)

app.include_router(auth_routes.router)
app.include_router(task_routes.router)

@app.get("/")
def root():
    return {"message": "Welcome to Assignment Task Tracker API"}
