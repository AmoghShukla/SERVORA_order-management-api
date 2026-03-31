from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from model.order import OrderCreate, OrderResponse  
from database.session import get_db
from service import order
from utils.loggers import logger

router = APIRouter(prefix="/orders", tags=['orders'])

@router.post('/', response_model=OrderResponse)
def create_order(payload : OrderCreate, db: Session = Depends(get_db)):
    try:
        return order.service_create_order(db)
    except HTTPException as e:
        raise f"{e}"