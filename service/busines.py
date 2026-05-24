from fastapi import HTTPException
from schemas import schemas
from db import models
from sqlalchemy.orm import Session
from random import randint
from security.auth import hash_pass, verify_pass, create_access_token, decode_access_token


def create_user(user: schemas.User, db: Session):
    db_user = db.query(models.User).filter(models.User.telephone == user.telephone).first()

    if db_user:
        raise HTTPException(status_code=400, detail='Такой пользователь уже имеется в базе!')

    random_cash = randint(0, 5000)
    hash_password = hash_pass(user.password)

    new_user = models.User(
        name=user.name,
        password=hash_password,
        telephone=user.telephone,
        cash=random_cash
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def clear_table(db: Session) -> dict:
    db.query(models.User).delete()
    db.commit()
    return {"message": "table cleared"}

def all_users(db: Session):
    users = db.query(models.User).all()
    return users

def user_for_id(user_id: int, db: Session):
    user = db.query(models.User).get(user_id)
    if user:
        return user
    raise HTTPException(status_code=404, detail='Такой пользователь не найден!')

def user_put(user_id: int, user_for_put: schemas.User, db: Session):
    user = db.query(models.User).get(user_id)
    if not user:
        HTTPException(status_code=404, detail='Такой пользователь не найден!')
    else:
        random_cash = randint(0, 5000)
        hashed_password = hash_pass(user_for_put.password)
        user.name = user_for_put.name
        user.password = hashed_password
        user.telephone = user_for_put.telephone
        user.cash = random_cash
        db.commit()
        return {"message": "user created!"}

def user_login(login: schemas.UserLogin, db: Session):
    user = db.query(models.User).filter(models.User.telephone==login.telephone).first()
    if not user or not verify_pass(login.password, user.password):
        raise HTTPException(status_code=501, detail='Неверный телефон или пароль!')
    return {"message": "Вы успешно вошли в приложение!"}