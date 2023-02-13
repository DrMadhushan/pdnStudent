"""_summary."""
import motor.motor_asyncio
from fastapi import HTTPException, status
from pymongo import ASCENDING

import config.database as dbconfig
from models.student import student_meta_objectify, student_objectify
from models.user import user_objectify

client = motor.motor_asyncio.AsyncIOMotorClient(dbconfig.HOST)
db = client.get_database(dbconfig.DATABASE_NAME)
students_collection = db.get_collection(dbconfig.STUDENTS_COLL)


async def get_all_students() -> list:
    """_summary.

    Raises:
        HTTPException: _description_
        HTTPException: _description_

    Returns:
        list: _description_
    """
    # Get all students name and img link in a given department and faculty
    students = []
    # Query database
    try:
        result = students_collection.find(
            {}, {"name": 1, "img": 1, "roll_no": 1, "_id": 0}
        ).sort(dbconfig.STUDENT_SCHEMA["roll_no"], ASCENDING)
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database error"
        ) from exc

    if result is None:
        # result from db is empty -> no such data found
        raise HTTPException(status_code=404, detail="Item not found")

    students_list = await result.to_list(None)

    for student in students_list:
        students.append(student_meta_objectify(student))

    return students


async def get_faculty_students(faculty) -> list:
    """_summary.

    Args:
        faculty (_type_): _description_

    Raises:
        HTTPException: _description_
        HTTPException: _description_

    Returns:
        list: _description_
    """
    students = []
    # Query database
    try:
        print(faculty)
        result = students_collection.find(
            {dbconfig.STUDENT_SCHEMA["faculty"]: faculty},
            projection={"name": 1, "img": 1, "roll_no": 1, "_id": 0},
        ).sort(dbconfig.STUDENT_SCHEMA["roll_no"], ASCENDING)
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database error"
        ) from exc

    if result is None:
        # result from db is empty -> no such data found
        raise HTTPException(status_code=404, detail="Item not found")

    students_list = await result.to_list(None)

    for student in students_list:
        students.append(student_meta_objectify(student))

    return students


async def get_department_students(faculty, department) -> list:
    """_summary.

    Args:
        faculty (_type_): _description_
        department (_type_): _description_

    Raises:
        HTTPException: _description_
        HTTPException: _description_

    Returns:
        list: _description_
    """
    students = []
    # Query database
    try:
        print(faculty, department)
        result = students_collection.find(
            {
                dbconfig.STUDENT_SCHEMA["faculty"]: faculty,
                dbconfig.STUDENT_SCHEMA["department"]: department,
            },
            {"name": 1, "img": 1, "roll_no": 1, "_id": 0},
        ).sort(dbconfig.STUDENT_SCHEMA["roll_no"], ASCENDING)
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database error: get_department_students",
        ) from exc

    if result is None:
        # result from db is empty -> no such data found
        raise HTTPException(status_code=404, detail="Item not found")

    students_list = await result.to_list(None)

    for student in students_list:
        students.append(student_meta_objectify(student))

    return students


async def get_student_info(roll_no: str) -> dict:
    """_summary.

    Args:
        roll_no (str): _description_

    Raises:
        HTTPException: _description_
        HTTPException: _description_

    Returns:
        dict: _description_
    """
    # Query database
    try:
        result = await students_collection.find_one(
            {dbconfig.STUDENT_SCHEMA["roll_no"]: roll_no}
        )
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database error when get student",
        ) from exc

    if result is None:
        # result from db is empty -> no such data found
        raise HTTPException(status_code=404, detail="Item not found")

    # print("result = ", result)

    student = student_objectify(result)
    return student


async def update_student_info(roll_no: str, update: dict):
    """_summary.

    Args:
        roll_no (str): _description_
        update (dict): _description_

    Raises:
        HTTPException: _description_
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    # Query database
    modification = update
    print(modification)
    new_name = update
    # for key in update.keys():

    try:
        result = await students_collection.update_one(
            {dbconfig.STUDENT_SCHEMA["roll_no"]: roll_no},
            {
                "$set": {
                    dbconfig.STUDENT_SCHEMA["new_name"]: new_name,
                    dbconfig.STUDENT_SCHEMA["updated"]: 1,
                }
            },
        )
    except HTTPException as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database error"
        ) from exc

    if result is None:
        # result from db is empty -> no such data found
        raise HTTPException(status_code=404, detail="Item not found")

    return {"message": "Successfully updated your profile!"}


async def get_all_profile_update_requests():
    """_summary.

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    profiles_to_verify = []
    # Query database
    try:
        result = students_collection.find(
            {dbconfig.STUDENT_SCHEMA["updated"]: 1},
            {"name": 1, "img": 1, "roll_no": 1, "_id": 0},
        )
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database error (profile update check)",
        ) from exc

    if result is None:
        # result from db is empty -> no such data found
        return {"message": "No recent update requests"}

    profiles_to_verify_list = await result.to_list(None)

    for profile in profiles_to_verify_list:
        profiles_to_verify.append(student_meta_objectify(profile))

    return profiles_to_verify


async def get_user_auth_data(email):
    """_summary.

    Args:
        email (_type_): _description_

    Raises:
        HTTPException: _description_

    Returns:
        dict: _description_
    """
    users_collection = db.get_collection(dbconfig.USERS_COLL)
    try:
        result = await users_collection.find_one(
            {dbconfig.USER_SCHEMA["email"]: email}, {"_id": 0}
        )
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database error (user data retrive)",
        ) from exc

    if result is None:
        return False
    # print("objectifying result")
    user = user_objectify(result)
    # print("objectified result")
    return user
