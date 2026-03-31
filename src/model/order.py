from sqlalchemy import Column, Integer, String, Float
from src.database.base import Base

class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    address = Column(String, nullable=False)
    total_price = Column(Float)
    order_status = Column(String)
    payment_status = Column(String)
    def __repr__(self):
        return f"<Order(order_id={self.order_id}, item_id={self.item_id}, quantity={self.quantity}, address='{self.address}', status='{self.status}', total_price='{self.total_price}', payment_status='{self.payment_status}')>"