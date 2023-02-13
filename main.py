"""_summary."""

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

from router import public, student, user
from services import auth
from services import database as db

app = FastAPI()
app.include_router(user.router)
app.include_router(student.router)
app.include_router(public.router)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/")
async def root(token: str = Depends(oauth2_scheme)):
    """_summary.

    Args:
        token (str, optional): _description_. Defaults to Depends(oauth2_scheme).

    Returns:
        _type_: _description_
    """
    user_details = await auth.get_current_user(token)
    return user_details


@app.get("/controls/admin/profile_updates")
async def get_all_profile_update_requests():
    """_summary.

    Returns:
        _type_: _description_
    """
    return await db.get_all_profile_update_requests()
