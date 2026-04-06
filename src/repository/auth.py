from fastapi import HTTPException
from model.user import User_Class


def repo_make_owner(user_id, db):
    user = db.query(User_Class).filter(User_Class.user_id == user_id).first()

    if not user:
        raise HTTPException(404, "User not found")

    user.role = "restaurant_owner"
    db.commit()

    return {"message": "User promoted to owner"}