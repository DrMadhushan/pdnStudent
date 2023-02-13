"""_summary."""


def student_objectify(student) -> dict:
    """_summary.

    Args:
        student (_type_): _description_

    Returns:
        dict: _description_
    """
    return {
        "name": student["name"],
        "new_name": student["name_update"],
        "roll_no": student["roll_no"],
        "batch": student["batch"],
        "faculty": student["faculty"],
        "department": student["department"],
        "interests": student["interests"],
        "img_src": student["img"],
        "updated": student["updated"],
    }


def student_meta_objectify(student) -> dict:
    """_summary.

    Args:
        student (_type_): _description_

    Returns:
        dict: _description_
    """
    return {
        "name": student["name"],
        "roll_no": student["roll_no"],
        "img_src": student["img"],
    }


def result_lister(object_lst) -> list:
    """_summary.

    Args:
        object (_type_): _description_

    Returns:
        list: _description_
    """
    return [student_objectify(item) for item in object_lst]
