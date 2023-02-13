from datetime import datetime, timedelta
import jwt
from passlib.hash import bcrypt
from fastapi import HTTPException, status, Depends
import services.database as db
from fastapi.security import OAuth2PasswordBearer
import config.auth as authconfig


async def authenticateUser(email: str, password: str):
    if email[-9:] != "pdn.ac.lk":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User from external organization",
        )

    # print("go to db")
    user = await db.getUserAuthData(email)
    # print("returned user from db")
    if not bcrypt.verify(password, user["password"]) or user == False:
        return False
    return user


def createJwt(user: dict) -> dict:
    expire = str(
        datetime.utcnow() + timedelta(minutes=authconfig.JWT_TOKEN_EXPIRE_MINUTES)
    )
    jwt_body = {
        "user_id": user["user_id"],
        "user_email": user["email"],
        "user_role": user["role"],
    }
    jwt_token = jwt.encode(
        jwt_body, authconfig.JWT_SECRET, algorithm=authconfig.JWT_ALGORITHM
    )
    return {"access_token": jwt_token, "token_type": "bearer", "expire": expire}


async def signInUser(email: str, password: str):
    # print("user try signin")
    user = await authenticateUser(email, password)
    if user == False:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid user credentials"
        )
    # print("authenticated")
    access_data = createJwt(user)
    return access_data


async def getCurrentUser(token: str):
    payload = jwt.decode(
        token, key=authconfig.JWT_SECRET, algorithms=[authconfig.JWT_ALGORITHM]
    )
    # print("payload = ", payload)
    return payload
