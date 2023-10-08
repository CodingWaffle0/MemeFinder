from flask import render_template, request

@app.route("/", methods = ["GET", "POST"])
def hello_world():
    if request.method == "POST":
        return render_template('index.html')
    else:
        return render_template('index.html')
    