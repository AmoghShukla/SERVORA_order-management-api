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
    