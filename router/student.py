"""_summary."""
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

# from services import auth
# from services import database as db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(
    prefix="/student",
    tags=["user"],
    dependencies=[Depends(oauth2_scheme)],
    responses={404: {"description": "Not Found"}},
)


@router.put("/edit/{roll_no}")
async def update_student_info(roll_no: str, update: dict):
    """_summary.

    Args:
        roll_no (str): _description_
        update (dict): _description_
        token (str, optional): _description_. Defaults to Depends(oauth2_scheme).

    Returns:
        _type_: _description_
    """
    # Update the student details
    print("update = ", type(update), roll_no)
    return update
    # return await db.update_student_info(roll_no, update)
