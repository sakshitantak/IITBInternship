import re
from flask import Flask
from flask import render_template, request
import math

app = Flask(__name__)

app.config.from_object(__name__)

internal_design_pressure = int(0)
vaccuum_pressure = int(0)
moment_ext_load = int(0)
moment_self_wt = int(0)
fluid_density = int(0)
design_temp = int(0)
num_layers = int(0)
L = int(0)
D = int(0)
Qc = int(0)
Qa = int(0)
Qp = int(0)
Do = int(0)
composite_density = int(0)
support_span = int(0)
thickness = int(0)
min_wall_thickness = int(0)
ulamphi = int(0)
ulamx = int(0)
circumferential_qc = 'Yes'
axial_qa = 'Yes'
axial_buckling_qa = 'Yes'

@app.route('/', methods=['POST', 'GET'])
def input_bs6464():
    return render_template('input_bs6464.html', 
    internal_design_pressure = internal_design_pressure,
    vaccuum_pressure = vaccuum_pressure,
    moment_ext_load = moment_ext_load,
    moment_self_wt = moment_self_wt,
    fluid_density = fluid_density,
    design_temp = design_temp,
    num_layers = num_layers,
    L = L,
    D = D,
    Qc = Qc,
    Qa = Qa,
    Qp = Qp,
    Do = Do,
    composite_density = composite_density,
    support_span = support_span,
    thickness = thickness,
    min_wall_thickness = min_wall_thickness,
    ulamphi = ulamphi,
    ulamx = ulamx,
    circumferential_qc = circumferential_qc,
    axial_qa = axial_qa,
    axial_buckling_qa = axial_buckling_qa
    )

@app.route('/calculate_after_input_bs6464', methods=['POST', 'GET'])
def calculate_after_input_bs6464():
    internal_design_pressure = int(0)
    vaccuum_pressure = request.form.get("vaccuum_pressure", type=float)
    moment_ext_load = request.form.get("moment_ext_load", type=float)
    moment_self_wt = request.form.get("moment_self_wt", type=float)
    fluid_density = request.form.get("fluid_density", type=float)
    design_temp = request.form.get("design_temp", type=float)
    #num_layers = request.form.get("num_layers", type=float)
    composite_density = request.form.get("composite_density", type=float)
    support_span = request.form.get("support_span", type=float)
    L = request.form.get("L", type=float)
    D = request.form.get("D", type=float)
    #Qc = request.form.get("Qc", type=float)
    #Qa = request.form.get("Qa", type=float)
    #Qp = request.form.get("Qp", type=float)
    #thickness = request.form.get("thickness", type=float)
    #min_wall_thickness = request.form.get("min_wall_thickness", type=float)
    #ulamphi = request.form.get("ulamphi", type=float)
    #ulamx = request.form.get("ulamx", type=float)
    #Do = request.form.get("Do", type=float)
    circumferential_qc = request.form.get("circumferential_qc", type=str)
    axial_qa = request.form.get("axial_qa", type=str)
    axial_buckling_qa = request.form.get("axial_buckling_qa", type=str)
    
    
    return render_template('input_bs6464.html',
    internal_design_pressure = internal_design_pressure,
    vaccuum_pressure = vaccuum_pressure,
    moment_ext_load = moment_ext_load,
    moment_self_wt = moment_self_wt,
    fluid_density = fluid_density,
    design_temp = design_temp,
    num_layers = num_layers,
    L = L,
    D = D,
    Qc = Qc,
    Qa = Qa,
    Qp = Qp,
    Do = Do,
    composite_density = composite_density,
    support_span = support_span,
    thickness = thickness,
    min_wall_thickness = min_wall_thickness,
    ulamphi = ulamphi,
    ulamx = ulamx,
    circumferential_qc = circumferential_qc,
    axial_qa = axial_qa,
    axial_buckling_qa = axial_buckling_qa
    )

@app.route('/laminates_bs6464', methods = ['POST', 'GET'])
def laminates_bs6464():
#     D = request.form.get("D", type=float)
#     if D is None:
#         D = 0

#     R = request.form.get("R", type=float)
#     if R is None:
#         R = 0

#     r = request.form.get("r", type=float)
#     if r is None:
#         r = 0

#     hi = request.form.get("hi", type=float)
#     if hi is None:
#         hi = 0

#     tb = request.form.get("tb", type=float)
#     if tb is None:
#         tb = 0

#     tk = request.form.get("tk", type=float)
#     if tk is None:
#         tk = 0
    
#     operation = request.form.get("operation")
#     result = 0
    
#     if operation == "Lc":
#         result = math.sqrt(D * tk) - 4 * (tk - tb)
#     elif operation == "Area":
#         result = 2 * math.pi * hi * R
#     else:
#         result = "INVALID CHOICE"
#     # result = {"Lc" : Lc,
#     #           "Area" : Area}
#     entry = result
    return render_template('laminates_bs6464.html')

if __name__ == '__main__':
    app.run(debug=True)