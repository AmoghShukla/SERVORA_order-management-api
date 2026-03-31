from fastapi import FastAPI, APIRouter
from src.routers.order_routers import router
from src.database.base import Base
from src.database.session import engine


app = FastAPI()
app.include_router(router, prefix="/Orders/api/v1", tags=['Orders'])

# Base.metadata.create_all(bind=engine)

app.get('/')
def HealthCheck():
    return {"message": "Welcome to the Order Management API!"}