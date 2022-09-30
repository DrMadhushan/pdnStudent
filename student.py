def student_objectify(student) -> dict:
    return {
        "name" : student['name'],
        "roll_no" : student['roll_no'],
        "batch" : student['batch'],
        "faculty" : student['faculty'],
        "department" : student['department'],
        "interests" : student['interests'],
        "img_src" : student['img']
    }

def student_meta_objectify(student) -> dict:
    return {
        "name" : student['name'],
        "roll_no" : student['roll_no'],
        "img_src" : student['img']
    }

def result_lister(object) -> list:
    return [student_objectify(item) for item in object]