"""_summary."""


def user_objectify(user) -> dict:
    """_summary.

    Args:
        user (_type_): _description_

    Returns:
        dict: _description_
    """
    return {
        "email": user["email"],
        "user_id": user["user_id"],
        "password": user["password"],
    }
