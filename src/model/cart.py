from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.orm import relationship
from src.database.base import Base

class Cart_Class(Base):
    __tablename__="Cart_Table"

    user_id = Column(Integer, ForeignKey('User_Table.user_id'), primary_key=True)
    order_id = Column(Integer, ForeignKey('Orders_Table.order_id'), primary_key=True)
    item_id = Column(Integer, ForeignKey('Items_Table.item_id'), primary_key=True)
    item_quantity = Column(Integer, nullable=False)

    item = relationship("Items_Class", back_populates="cart_entries")
    order = relationship("Order_Class", back_populates="cart_entries")