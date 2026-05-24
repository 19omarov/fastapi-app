from datetime import datetime, timedelta, timezone
import jwt
from jwt import PyJWTError
from passlib.context import CryptContext




pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "super-secret-key-change-me-right-now-12345"
ALGORITHM = "HS256"




def hash_pass(password: str):
    return pwd_context.hash(password)

def verify_pass(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(user: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = user.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def decode_access_token(token: str) -> str | None:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            return None
        return username
    except PyJWTError:
        return None
