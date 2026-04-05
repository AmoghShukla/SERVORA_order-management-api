from src.middleware.loggers import get_logger
from sqlalchemy.orm import Session
from src.model.user import User_Class
from sqlalchemy.exc import SQLAlchemyError
from src.exceptions.custom_exception import RepositoryError, ServiceError, NotFoundError 
from pydantic import EmailStr

logger = get_logger(__name__)

def get_user_by_email(email : EmailStr, db : Session):
    try:
        user = db.query(User_Class).filter(User_Class.user_email==email).first()
        if not user:
            raise NotFoundError(f"Task with Email ID : {email}, Does not exist")
    except SQLAlchemyError as e:
        raise RepositoryError("Failed to Fetch User with Email : {email}") from e

def create_user(payload, db : Session):
    try:
        new_user = User_Class(
            user_name = payload.user_name,
            user_phone = payload.user_phone,
            user_email = payload.user_email,
            user_password=payload.user_password,
            user_role=payload.user_role if hasattr(payload, "user_role") else "USER"
        )
        logger.info(f"Creating user with payload: {payload}")
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        logger.info(f"Order created successfully: {new_user}")
        return new_user
    except SQLAlchemyError as e:
        db.rollback()
        raise RepositoryError("Failed to Create User") from e

def get_user(user_id : int, db : Session):
    try:
        user = db.query(User_Class).filter(User_Class.user_id==user_id).first()
        if user:
            return user
    except Exception as e:
        print(e)
        return None

