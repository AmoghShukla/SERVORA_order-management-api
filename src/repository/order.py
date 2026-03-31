from utils.loggers import logger
from typing import Session

def create_order(payload, db: Session):
    try:
        new_order = {
            "order_id": payload.order_id,
            "item_id": payload.item_id,
            "quantity": payload.quantity, 
            "address": payload.address
        }
        logger.info(f"Creating order with payload: {payload}")
        db.add(new_order)
        db.commit()
        db.refresh(new_order)
        logger.info(f"Order created successfully: {new_order}")
        return new_order
    except Exception as e:
        logger.error(f"Error creating order: {e}")
        raise Exception(f"Error creating order: {e}")