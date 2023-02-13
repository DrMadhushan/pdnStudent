"""_summary."""
from fastapi import APIRouter, Depends, Form
from fastapi.security import OAuth2PasswordBearer

from services import auth

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(
    prefix="/user", tags=["user"], responses={404: {"description": "Not Found"}}
)


@router.get("/")
async def get_user(token: str = Depends(oauth2_scheme)):
    """_summary.

    Args:
        token (str, optional): _description_. Defaults to Depends(oauth2_scheme).

    Returns:
        _type_: _description_
    """
    print("hello")
    user_details = await auth.get_current_user(token)
    return user_details


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
