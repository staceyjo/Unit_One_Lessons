def get_fire_students(students):
    '''
    INPUT: A list of dictionaries with the "name" and "class" key-value pairs.
    Example:  get_fire_students([{ "name": "Ada", "class": "fire"}, { "name": "Taylor", "class": "earth" }])
    RETURN VALUE: A list of dictionaries with **only** the students in the "fire" class.
    '''
    temp = []
    
    while students:
        student = students.pop()
        if student["class"] == "fire":
            temp.append(student)

    while temp:
        students.append(temp.pop())

    print(students)
    return students

get_fire_students([{ "name": "Ada", "class": "fire"}, { "name": "Taylor", "class": "earth" }])