from fastapi import APIRouter, Depends, Form
from fastapi.security import OAuth2PasswordBearer
import services.auth as auth

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(
    prefix="/user", tags=["user"], responses={404: {"description": "Not Found"}}
)


@router.get("/")
async def getUser(token: str = Depends(oauth2_scheme)):
    print("hello")
    user_details = await auth.getCurrentUser(token)
    return user_details


@router.post("/signin")
async def signInUser(email: str = Form(), password: str = Form()):
    # print("user try signin")
    access_data = await auth.signInUser(email, password)
    return access_data
