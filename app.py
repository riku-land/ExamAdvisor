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

    return f"""
    偏差値 : {score}<br>
    学部 : {faculty}<br>
    地域 : {area}
    """

def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)