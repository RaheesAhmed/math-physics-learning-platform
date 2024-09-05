from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import math_routes, physics_routes
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(math_routes.router, prefix="/api/math", tags=["math"])
app.include_router(physics_routes.router, prefix="/api/physics", tags=["physics"])


@app.get("/")
async def root():
    return {"message": "Welcome to the Math and Physics Educational Platform API"}
