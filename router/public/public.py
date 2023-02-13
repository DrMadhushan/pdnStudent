from fastapi import APIRouter
import services.database as db

router = APIRouter(
    prefix="/public", tags=["user"], responses={404: {"description": "Not Found"}}
)


@router.get("/students")
async def getStudents():
    # Get all students name and img link
    return await db.getAllStudents()


@router.get(
    "/students/{faculty}",
)
async def getFacultyStudents(faculty: str):
    # Get all students name and img link in a given faculty
    return await db.getFacultyStudents(faculty)


@router.get("/students/{faculty}/{department}")
async def getDepartmentStudents(faculty: str, department: str):
    # Get all students name and img link in a given department and faculty
    return await db.getDepartmentStudents(faculty, department)


@router.get("/student/view/{roll_no}")
async def getStudentInfo(roll_no: str):
    # returns the requested student's details
    return await db.getStudentInfo(roll_no)
