from flask import Flask, render_template, request, session
import Controller
import json


app = Flask(__name__)

@app.route("/")
@app.route("/index")
def display_homepage():
    return render_template("index.html", the_title="SpellChecker")
    controller = Controller()
    controller.loadModel()


@app.route("/index", methods=["POST"])
def determine_cheats():
    session["previous"] = pattern = request.form["pattern"]
    session["count"] = 0
    matches = Controller.find_possible_matches(pattern)
    return render_template(
        "results.html", the_title="Here are your results", data=sorted(matches)
    )


## You do NOT need to port the next two functions. ########


@app.route("/session")
def show_session():
    session["count"] += 1
    return f"The previous pattern is: {session['previous']} and the count is {session['count']}."


@app.route("/api/cheat/<pattern>")
def return_correction(pattern):
    matches = Controller.find_possible_matches(pattern)
    return json.dumps(sorted(matches))


app.secret_key = "dskfjdfdg igvk gereregopritr re"


if __name__ == "__main__":
    app.run(debug=True)
