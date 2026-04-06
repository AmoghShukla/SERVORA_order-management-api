from fastapi import HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from src.schema.user import UserCreate, UserLogin, Token, RefreshTokenRequest
from src.database.session import get_db
from src.service.auth import SignUp, login, service_make_owner, refresh_access_token
from src.dependencies.auth import require_role
from src.exceptions.custom_exception import ServiceError


router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/signup")
def Signup_user(payload : UserCreate, db : Session = Depends(get_db)):
    return SignUp(payload, db)

@router.post("/login", response_model=Token)
def login_user(payload: UserLogin, db: Session = Depends(get_db)):
    return login(payload, db)

@router.post("/refresh", response_model=Token)
def refresh_token(payload: RefreshTokenRequest):
    try:
        return refresh_access_token(payload.refresh_token)
    except ServiceError as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.patch("/users/{user_id}/make-owner")
def make_owner(
    user_id: int,
    db: Session = Depends(get_db),
    admin = Depends(require_role(['ADMIN']))
):
    return service_make_owner(user_id, db)
