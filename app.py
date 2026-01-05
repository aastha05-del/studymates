from flask import Flask, render_template, request
from courses import load_courses, get_course
from study_mode import generate_practice_questions
from progress import update_progress, get_progress

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/courses")
def courses():
    return render_template("courses.html", courses=load_courses())

@app.route("/study", methods=["GET", "POST"])
def study():
    course = None
    questions = []

    if request.method == "POST":
        course_name = request.form["course"]
        course = get_course(course_name)
        questions = generate_practice_questions(course_name)
        update_progress(course_name)

    return render_template("study.html", course=course, questions=questions)

@app.route("/progress")
def progress():
    return render_template("progress.html", progress=get_progress())

if __name__ == "__main__":
    app.run(debug=True)
