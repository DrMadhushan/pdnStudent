from fastapi import APIRouter, Depends, Form
from fastapi.security import OAuth2PasswordBearer
import services.auth as auth
import services.database as db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(
    prefix="/student",
    tags=["user"],
    dependencies=[Depends(oauth2_scheme)],
    responses={404: {"description": "Not Found"}},
)


@router.put("/edit/{roll_no}")
async def updateStudentInfo(
    roll_no: str, update: dict, token: str = Depends(oauth2_scheme)
):
    # Update the student details
    print("update = ", type(update))
    return update
    return await db.updateStudentInfo(roll_no, new_name)
