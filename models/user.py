def user_objectify(user) -> dict:
    return {
        "email": user["email"],
        "user_id": user["user_id"],
        "password": user["password"],
    }
