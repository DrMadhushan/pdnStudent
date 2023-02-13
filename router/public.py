"""_summary."""
from fastapi import APIRouter

from services import database as db

router = APIRouter(
    prefix="/public", tags=["user"], responses={404: {"description": "Not Found"}}
)


@router.get("/students")
async def get_students():
    """_summary.

    Returns:
        _type_: _description_
    """
    # Get all students name and img link
    return await db.get_all_students()


@router.get(
    "/students/{faculty}",
)
async def get_faculty_students(faculty: str):
    """_summary.

    Args:
        faculty (str): _description_

    Returns:
        _type_: _description_
    """
    # Get all students name and img link in a given faculty
    return await db.get_faculty_students(faculty)


@router.get("/students/{faculty}/{department}")
async def get_department_students(faculty: str, department: str):
    """_summary.

    Args:
        faculty (str): _description_
        department (str): _description_

    Returns:
        _type_: _description_
    """
    # Get all students name and img link in a given department and faculty
    return await db.get_department_students(faculty, department)


@router.get("/student/view/{roll_no}")
async def get_student_info(roll_no: str):
    """_summary.

    Args:
        roll_no (str): _description_

    Returns:
        _type_: _description_
    """
    # returns the requested student's details
    return await db.get_student_info(roll_no)
