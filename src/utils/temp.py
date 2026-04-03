from fastapi import Header, HTTPException, Depends
from src.utils.storage import sessions

def get_current_user(x_session_id: str = Header(...)):
    user = sessions.get(x_session_id)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid session")

    return user