import motor.motor_asyncio
from pymongo import MongoClient, DESCENDING, ASCENDING
from bson.objectid import ObjectId
from student import student_meta_objectify, student_objectify
from user import user_objectify
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
        result = students_collection.find({}, {'name':1, 'img':1, 'roll_no':1, '_id':0}).sort(dbconfig.STUDENT_SCHEMA["roll_no"], ASCENDING)
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
        result = await students_collection.find({dbconfig.STUDENT_SCHEMA["faculty"] : faculty}, {'name':1, 'img':1, 'roll_no':1, '_id':0}).sort(dbconfig.STUDENT_SCHEMA["roll_no"], ASCENDING)
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
        result = await students_collection.find({{dbconfig.STUDENT_SCHEMA["faculty"] : faculty, dbconfig.STUDENT_SCHEMA["department"]: department}}, {'name':1, 'img':1, 'roll_no':1, '_id':0}).sort(dbconfig.STUDENT_SCHEMA["roll_no"], ASCENDING)
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database error")
    
    if result == None:
        # result from db is empty -> no such data found
        raise HTTPException(status_code=404, detail="Item not found")
        
    students_list = await result.to_list(None)

    for student in students_list:
        students.append(student_meta_objectify(student))
    
    return students

async def getStudentInfo(roll_no: str) -> dict:
    # Query database
    try:
        result = await students_collection.find_one({ dbconfig.STUDENT_SCHEMA["roll_no"] : roll_no})
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database error when get student")

    if result == None: 
        # result from db is empty -> no such data found
        raise HTTPException(status_code=404, detail="Item not found")
    
    # print("result = ", result)

    student = student_objectify(result)
    return student

async def updateStudentInfo(roll_no, new_name):
    # Query database
    try:
        result = await students_collection.update_one(
                {dbconfig.STUDENT_SCHEMA["roll_no"]: roll_no}, 
                {'$set' : {
                    dbconfig.STUDENT_SCHEMA["new_name"] : new_name, 
                    dbconfig.STUDENT_SCHEMA["updated"] : 1
                    }
                }
            )
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database error")
    
    if result == None: 
        # result from db is empty -> no such data found
        raise HTTPException(status_code=404, detail="Item not found")
    
    return {"message" : "Successfully updated your profile!"}

async def getAllProfileUpdateRequests():
    profiles_to_verify = []
    # Query database
    try:
        result = students_collection.find({dbconfig.STUDENT_SCHEMA["updated"] : 1}, {'name':1, 'img':1, 'roll_no':1, '_id':0})
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database error (profile update check)")
    
    if result == None:
        # result from db is empty -> no such data found
        return {"message" : "No recent update requests"}
        
    profiles_to_verify_list = await result.to_list(None)

    for profile in profiles_to_verify_list:
        profiles_to_verify.append(student_meta_objectify(profile))
    
    return profiles_to_verify

async def getUserAuthData(email) -> dict:
    users_collection = db.get_collection(dbconfig.USERS_COLL)
    try:
        result = await users_collection.find_one({dbconfig.USER_SCHEMA["email"] : email}, {"_id" : 0})
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database error (user data retrive)")
    
    if result == None:
        return False
    print("objectifying result")
    user = user_objectify(result)
    print("objectified result")
    return user
