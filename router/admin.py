"""_summary."""
from fastapi import APIRouter, Form
from fastapi.security import OAuth2PasswordBearer

from services import auth
from services import database as db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(
    prefix="/admin", tags=["admin"], responses={404: {"description": "Not Found"}}
)


@router.get("/profile_update_requests")
async def get_all_profile_update_requests():
    """_summary.

    Returns:
        _type_: _description_
    """
    return await db.get_all_profile_update_requests()


@router.post("/signin")
async def sign_in_user(email: str = Form(), password: str = Form()):
    """_summary.

    Args:
        email (str, optional): _description_. Defaults to Form().
        password (str, optional): _description_. Defaults to Form().

    Returns:
        _type_: _description_
    """
    # print("user try signin")
    access_data = await auth.sign_in_user(email, password)
    return access_data
