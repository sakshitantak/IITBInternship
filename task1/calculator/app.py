from flask import Flask
from flask import render_template, request
import math

app = Flask(__name__)

app.config.from_object(__name__)

@app.route('/')
def welcome():
    return render_template('form.html')

@app.route('/result', methods = ['POST'])
def result():
    D = request.form.get("D", type=float)
    R = request.form.get("R", type=float)
    r = request.form.get("r", type=float)
    hi = request.form.get("hi", type=float)
    tb = request.form.get("tb", type=float)
    tk = request.form.get("tk", type=float)
    operation = request.form.get("operation")

    if operation == "Lc":
        result = math.sqrt(D * tk) - 4 * (tk - tb)
    elif operation == "Area":
        result = 2 * math.pi * hi * R
    else:
        result = "INVALID CHOICE"
    # result = {"Lc" : Lc,
    #           "Area" : Area}
    entry = result
    return render_template('result.html', entry = entry)

if __name__ == '__main__':
    app.run(debug=True)