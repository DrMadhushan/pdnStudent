"""_summary."""
HOST = "mongodb://localhost:27017"
DATABASE_NAME = "pdnPeople"
STUDENTS_COLL = "students"
STAFF_COLL = "staff"
USERS_COLL = "users"

STUDENT_SCHEMA = {
    "student_name": "name",
    "new_name": "name_update",
    "roll_no": "roll_no",
    "batch": "batch",
    "faculty": "faculty",
    "department": "department",
    "interests": "interests",
    "img_link": "img",
    "updated": "updated",
}

USER_SCHEMA = {"email": "email", "user_id": "user_id", "pwd": "password"}
