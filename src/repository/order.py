from src.utils.loggers import get_logger
from sqlalchemy.orm import Session
from src.schema.order import OrderCreate
from src.model.order import Order

logger = get_logger(__name__)

def create_order(payload, db: Session):
    try:
        data = payload.model_dump()

        new_order = Order(
            item_id=data["item_id"],
            quantity=data["quantity"],
            address=data["address"],
            # total_price=calculate_price(data["item_id"], data["quantity"])
            total_price=12,  # if exists
            order_status="PENDING",
            payment_status="UNPAID"
        )
        logger.info(f"Creating order with payload: {payload}")
        db.add(new_order)
        db.commit()
        db.refresh(new_order)
        logger.info(f"Order created successfully: {new_order}")
        return new_order
    except Exception as e:
        logger.error(f"Error creating order: {e}")
        raise Exception(f"Error creating order: {e}")