from fastapi import APIRouter, Depends
from schemas import schemas
from typing import List
from service import busines as us
from sqlalchemy.orm import Session
from db.database import get_db
from security.auth import decode_access_token



router = APIRouter(
    prefix='/users',
    tags=['BBank']
)

@router.post('/user_create', response_model=schemas.UserResponse)
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    return us.create_user(user=user, db=db)

@router.delete('/table_clear')
def clear_table(db: Session=Depends(get_db)) -> dict:
    return us.clear_table(db=db)

@router.get('/users_all', response_model=List[schemas.UserResponse])
def all_users(db: Session=Depends(get_db)):
    return us.all_users(db=db)

@router.get('/user_for_id/{user_id}', response_model=schemas.UserResponse)
def user_for_id(user_id: int, db: Session=Depends(get_db)):
    return us.user_for_id(user_id=user_id, db=db)

@router.put('/user_put/{user_id}')
def user_put(user_id: int, user_for_put: schemas.User, db: Session=Depends(get_db)) -> dict:
    return us.user_put(user_id=user_id, user_for_put=user_for_put, db=db)

@router.post('/user_login')
def user_login(login: schemas.UserLogin, db: Session=Depends(get_db)) -> dict:
    return us.user_login(login=login, db=db)