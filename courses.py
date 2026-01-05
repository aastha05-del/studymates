import json

def load_courses():
    with open("data/courses.json", "r") as file:
        return json.load(file)

def get_course(course_name):
    courses = load_courses()
    return courses.get(course_name)
