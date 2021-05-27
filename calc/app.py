# Put your app in here.
from flask import Flask
from flask import request
import operations

app = Flask(__name__)

@app.route("/add")
def ap_add():
    
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operations.add(a, b)

    return str(result)

@app.route("/sub")
def ap_sub():
    
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operations.sub(a, b)

    return str(result)

@app.route("/mult")
def ap_mult():
    
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operations.mult(a, b)

    return str(result)

@app.route("/div")
def ap_div():
    
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operations.div(a, b)

    return str(result)

oper_dict = {
    'add': operations.add,
    'sub': operations.sub,
    'mult': operations.mult,
    'div': operations.div
}

@app.route('/math/<operation>')
def ap_oper(operation):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = oper_dict[operation](a,b)
    return str(result)
