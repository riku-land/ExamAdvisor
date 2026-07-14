from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():

    score = request.form["score"]
    faculty = request.form["faculty"]
    area = request.form["area"]

    return render_template(
        "result.html",
        score=score,
        faculty=faculty,
        area=area
    )

def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)