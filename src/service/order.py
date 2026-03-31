from typing import Session
from utils.loggers import logger
from repository import order

def service_create_order(payload, db : Session):
    try:
        return order.create_order(payload, db)
    except Exception as e:
        logger.error(f"Error creating order: {e}")
        raise Exception(f"Error creating order: {e}")