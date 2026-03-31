from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.schema.order import OrderCreate, OrderResponse  
from src.database.session import get_db
from src.service.order import service_create_order
from src.utils.loggers import get_logger

logger = get_logger(__name__)

router = APIRouter(prefix="/orders", tags=['orders'])

@router.post('/')
def create_order(payload : OrderCreate, db: Session = Depends(get_db)):
    try:
        return service_create_order(payload, db)
    except Exception as e:
        logger.error(f"Error creating order: {e}")
        raise HTTPException(status_code=500, detail=str(e))