from sqlalchemy.orm import relationship
from sqlalchemy import Integer, Float, String, Column
from src.database.base import Base

class User_Class(Base):
    __tablename__="User_Table"

    user_id = Column(Integer, nullable=False, primary_key=True)
    user_name = Column(String, nullable=False)
    user_phone = Column(Integer, nullable=False)
    user_email = Column(Integer, nullable=False)

    Orders = relationship("Order", back_populates="Orders_Table")