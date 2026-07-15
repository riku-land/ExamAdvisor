from flask import Flask, render_template, request

import json

app = Flask(__name__)

def load_universities():

    with open(
        "data/universities.json",
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)

def recommend_universities(score, faculty, area):

    universities = load_universities()

    result = []

    for university in universities:

        if (
            university["faculty"] == faculty
            and university["area"] == area
            and university["score"] <= score
        ):
            result.append(university["name"])

    return result[:3]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():

    score_text = request.form["score"]
    faculty = request.form["faculty"]
    area = request.form["area"]


    if score_text == "":
        return render_template(
            "error.html",
            message="偏差値を入力してください"
        )

    score = int(score_text)

    if score < 20 or score > 80:
        return render_template(
            "error.html",
            message="偏差値は20~80で入力してください"
        )
    

    universities = recommend_universities(
        score,
        faculty,
        area
    )

    return render_template(
        "result.html",
        score=score,
        faculty=faculty,
        area=area,
        recommended_universities=universities
    )

if __name__ == "__main__":
    app.run(debug=True)