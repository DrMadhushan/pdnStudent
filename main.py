# main.py

from datetime import datetime, timedelta
from fastapi import Depends, FastAPI, status, Form, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
import jwt
from passlib.hash import bcrypt

import database as db

JWT_SECRET = "secret_key"
JWT_ALGORITHM = "HS256"
JWT_TOKEN_EXPIRE_MINUTES = 5

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

# @app.post("/signin")
# async def signInUser(email: str = Form(), password: str = Form()):
#     print("user try signin")
#     user = await authenticateUser(email, password)
#     if user == False:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User from external organization")
#     print("authenticated")
#     access_data = createJwt(user)
#     return access_data

# async def authenticateUser(email: str, password: str):
#     if email[-9:] != "pdn.ac.lk":
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User from external organization")
    
#     print("go to db")
#     user = await db.getUserAuthData(email)
#     print("returned user from db")
#     if not bcrypt.verify(password, user["password"]) or user == False:
#         return False
#     return user
    
def createJwt(user: dict) -> dict:
    expire = datetime.utcnow() + timedelta(minutes=JWT_TOKEN_EXPIRE_MINUTES)
    jwt_body = { "user_id" : user["user_id"], "user_email": user["email"]}
    jwt_token = jwt.encode(jwt_body, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return {"access_token" : jwt_token, "token_type" : "bearer"}
