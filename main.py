# main.py

from fastapi import Depends, FastAPI, status, Form
from fastapi.security import OAuth2PasswordBearer
import database as db
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "No Functionality"}

@app.get("/students")
async def getStudents():
    # Get all students name and img link
    return await db.getAllStudents()

@app.get("/students/{faculty}")
async def getFacultyStudents(faculty: str):
    # Get all students name and img link in a given faculty
    return await db.getFacultyStudents(faculty)

@app.get("/students/{faculty}/{department}")
async def getDepartmentStudents(faculty: str, department: str):
    # Get all students name and img link in a given department and faculty 
    return await db.getDepartmentStudents(faculty, department)   

@app.get("/student/view/{roll_no}")
async def getStudentInfo(roll_no: str):
    # returns the requested student's details
    return await db.getStudentInfo(roll_no)

@app.put("/student/edit/{roll_no}")
async def updateStudentInfo(roll_no: str, new_name: str = Form()):
    # Update the student details
    return await db.updateStudentInfo(roll_no, new_name)

@app.get("/controls/admin/profile_updates")
async def getAllProfileUpdateRequests():
    return await db.getAllProfileUpdateRequests()


'''
@app.get("/students/{roll_no}")
async def getStudentInfo(roll_no: str):
    # returns the requested student's details
    return await db.getStudentInfo(roll_no)
'''