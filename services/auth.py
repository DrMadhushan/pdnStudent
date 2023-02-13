"""_summary."""
from datetime import datetime, timedelta

import jwt
from fastapi import HTTPException, status
from passlib.hash import bcrypt

from config import auth as authconfig
from services import database as db


async def authenticate_user(email: str, password: str):
    """_summary.

    Args:
        email (str): _description_
        password (str): _description_

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    if email[-9:] != "pdn.ac.lk":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User from external organization",
        )

    # print("go to db")
    user = await db.get_user_auth_data(email)
    # print("returned user from db")
    if not bcrypt.verify(password, user["password"]) or user is False:
        return False
    return user


def create_jwt(user: dict) -> dict:
    """_summary.

    Args:
        user (dict): _description_

    Returns:
        dict: _description_
    """
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


async def sign_in_user(email: str, password: str):
    """_summary.

    Args:
        email (str): _description_
        password (str): _description_

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    # print("user try signin")
    user = await authenticate_user(email, password)
    if user is False:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid user credentials"
        )
    # print("authenticated")
    access_data = create_jwt(user)
    return access_data


async def get_current_user(token: str):
    """_summary.

    Args:
        token (str): _description_

    Returns:
        _type_: _description_
    """
    payload = jwt.decode(
        token, key=authconfig.JWT_SECRET, algorithms=[authconfig.JWT_ALGORITHM]
    )
    # print("payload = ", payload)
    return payload
