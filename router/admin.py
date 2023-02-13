from fastapi import APIRouter, Depends, Form
from fastapi.security import OAuth2PasswordBearer
import services.auth as auth

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(
    prefix="/admin", tags=["admin"], responses={404: {"description": "Not Found"}}
)


@router.get("/profile_update_requests")
async def getAllProfileUpdateRequests():
    return await db.getAllProfileUpdateRequests()


@router.post("/signin")
async def signInUser(email: str = Form(), password: str = Form()):
    # print("user try signin")
    access_data = await auth.signInUser(email, password)
    return access_data
