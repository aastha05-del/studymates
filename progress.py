progress_data = {}

def update_progress(course):
    if course in progress_data:
        progress_data[course] += 10
    else:
        progress_data[course] = 10

def get_progress():
    return progress_data
