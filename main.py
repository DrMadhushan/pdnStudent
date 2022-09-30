# main.py

from fastapi import Depends, FastAPI, status
from fastapi.security import OAuth2PasswordBearer
import database as db
from pydantic import BaseModel

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/students/")
async def getStudents():
    # Get all students name and img link
    students = await db.getAllStudents()
    return students

@app.get("/students/{roll_no}")
async def getStudentInfo1(roll_no: str):
    # returns the requested student's details
    student = await db.getStudentInfo(roll_no)
    return student

@app.get("/students/{faculty}")
async def getFacultyStudents(faculty: str):
    # Get all students name and img link in a given faculty
    students = await db.getFacultyStudents(faculty)
    return students

@app.get("/students/{faculty}/{roll_no}")   # , status_code=status.HTTP_202_ACCEPTED
async def getStudentInfo2(roll_no: str):
    # returns the requested student's details
    student = await db.getStudentInfo(roll_no)
    return student

@app.get("/students/{faculty}/{department}")
async def getDepartmentStudents(faculty: str, department: str):
    # Get all students name and img link in a given department and faculty
    students = await db.getDepartmentStudents(faculty, department)   
    return students

@app.get("/students/{faculty}/{department}/{roll_no}")
async def getStudentInfo3(roll_no: str):
    # returns the requested student's details
    student = await db.getStudentInfo(roll_no)
    return student

class Student(BaseModel):
    id : str
    name : str
    batch : str
    faculty : str
    department : str
    interests : list
    img_src : str

def student_objectify(student) -> Student:
    return {
    "name" : student['name'],
    "batch" : student['batch'],
    "faculty" : student['faculty'],
    "department" : student['department'],
    "interests" : student['interests'],
    "img_src" : student['img'] 
    }

