# main.py

from fastapi import Depends, FastAPI, status
from fastapi.security import OAuth2PasswordBearer
import database as db
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/students/")
async def getStudents():
    # Get all students name and img link
    students = await db.getAllStudents()
    return students

@app.get("/students/{roll_no}")
async def getStudentInfo(roll_no: str):
    # returns the requested student's details
    student = await db.getStudentInfo(roll_no)
    return student

@app.get("/students/{faculty}")
async def getFacultyStudents(faculty: str):
    # Get all students name and img link in a given faculty
    students = await db.getFacultyStudents(faculty)
    return students

@app.get("/{faculty}/students/{roll_no}")   # , status_code=status.HTTP_202_ACCEPTED
async def getStudentInfo(roll_no: str, faculty: str):
    # returns the requested student's details
    student = await db.getStudentInfo(roll_no, faculty)
    return student

@app.get("/students/{faculty}/{department}")
async def getDepartmentStudents(faculty: str, department: str):
    # Get all students name and img link in a given department and faculty
    students = await db.getDepartmentStudents(faculty, department)   
    return students

@app.get("/{faculty}/{department}/students/{roll_no}")
async def getStudentInfo(roll_no: str, faculty: str, department: str):
    # returns the requested student's details
    student = await db.getStudentInfo(roll_no, faculty, department)
    return student