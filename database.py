import motor.motor_asyncio
from pymongo import MongoClient, DESCENDING, ASCENDING
from bson.objectid import ObjectId
from student import student_meta_objectify, student_objectify
import config.database as dbconfig
from fastapi import HTTPException, status


client = motor.motor_asyncio.AsyncIOMotorClient(dbconfig.HOST)
db = client.get_database(dbconfig.DATABASE_NAME)
students_collection = db.get_collection(dbconfig.STUDENTS_COLL)

async def getAllStudents() -> list:
    # Get all students name and img link in a given department and faculty
    students = []
    # Query database
    try:
        result = students_collection.find({}, {'name':1, 'img':1, 'roll_no':1, '_id':0})
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database error")
    
    if result == None:
        # result from db is empty -> no such data found
        raise HTTPException(status_code=404, detail="Item not found")
        
    students_list = await result.to_list(None)

    for student in students_list:
        students.append(student_meta_objectify(student))
    
    return students

async def getFacultyStudents(faculty) -> list:
    students = []
    # Query database
    try:
        result = students_collection.find({dbconfig.STUDENT_SCHEMA["faculty"] : faculty}, {'name':1, 'img':1, 'roll_no':1, '_id':0}).sort(dbconfig.STUDENT_SCHEMA["roll_no"], ASCENDING)
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database error")
    
    if result == None:
        # result from db is empty -> no such data found
        raise HTTPException(status_code=404, detail="Item not found")
        
    students_list = await result.to_list(None)

    for student in students_list:
        students.append(student_meta_objectify(student))
    
    return students

async def getDepartmentStudents(faculty, department) -> list:
    students = []
    # Query database
    try:
        result = students_collection.find({{dbconfig.STUDENT_SCHEMA["faculty"] : faculty, dbconfig.STUDENT_SCHEMA["department"]: department}}, {'name':1, 'img':1, 'roll_no':1, '_id':0}).sort(dbconfig.STUDENT_SCHEMA["roll_no"], ASCENDING)
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database error")
    
    if result == None:
        # result from db is empty -> no such data found
        raise HTTPException(status_code=404, detail="Item not found")
        
    students_list = await result.to_list(None)

    for student in students_list:
        students.append(student_meta_objectify(student))
    
    return students

async def getStudentInfo(roll_no: str, faculty: str = None, department: str = None) -> dict:
    # Query database
    try:
        if faculty == None:
            result = await students_collection.find_one({ dbconfig.STUDENT_SCHEMA["roll_no"] : roll_no})
        elif department == None:
            result = await students_collection.find_one({ dbconfig.STUDENT_SCHEMA["roll_no"] : roll_no, dbconfig.STUDENT_SCHEMA["faculty"]: faculty})
        else:
            result = await students_collection.find_one({ dbconfig.STUDENT_SCHEMA["roll_no"] : roll_no, dbconfig.STUDENT_SCHEMA["faculty"]: faculty, dbconfig.STUDENT_SCHEMA["department"]: department})
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database error")

    if result == None: 
        # result from db is empty -> no such data found
        raise HTTPException(status_code=404, detail="Item not found")

    student = student_objectify(result)
    return student
