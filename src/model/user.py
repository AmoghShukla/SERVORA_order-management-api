from sqlalchemy.orm import relationship
from sqlalchemy import Integer, Float, String, Column
from src.database.base import Base

class User_Class(Base):
    __tablename__ = "User_Table"

    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String)
    user_phone = Column(String)
    user_email = Column(String)

    orders = relationship("Order_Class", back_populates="user")