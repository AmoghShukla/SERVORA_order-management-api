from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from uuid import uuid4

from src.routers.user_routers import get_user
from src.utils.storage import sessions
from src.database.session import get_db


router = APIRouter(prefix="/auth", tags=["Login"])

@router.get('/login')
def login(user_id: int, database: Session = Depends(get_db)):
    user = get_user(user_id, database)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid user")
    
    session_id = str(uuid4())
    sessions[session_id] = user


    return {
        "session_id": session_id,
        "user": user
    }





