"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github)
    return html


@app.route("/student-search")
def get_student_form():
	"""Show form for searching for a student."""

	return render_template("student_search.html")


# @app.route("/student-add", methods=["GET", "POST"])
@app.route("/student-add", methods=["POST"])
def show_confirmation():
	"""adds a student to the table"""

	# if request.method == "POST":

	first = request.form.get("first_name")
	last = request.form.get("last_name")
	gh = request.form.get("github")

	hackbright.make_new_student(first, last, gh)

	return render_template('confirmation.html',user_name=gh)
	# elif request.method == "GET":
		# add student


@app.route("/new-student")
def add_new_student():
	""" get new student info """
	return render_template("add_student.html")





if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
