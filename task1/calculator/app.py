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
    if D is None:
        D = 0

    R = request.form.get("R", type=float)
    if R is None:
        R = 0

    r = request.form.get("r", type=float)
    if r is None:
        r = 0

    hi = request.form.get("hi", type=float)
    if hi is None:
        hi = 0

    tb = request.form.get("tb", type=float)
    if tb is None:
        tb = 0

    tk = request.form.get("tk", type=float)
    if tk is None:
        tk = 0
    
    operation = request.form.get("operation")
    result = 0
    
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