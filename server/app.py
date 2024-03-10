#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return param

@app.route('/count/<int:param>')
def count(param):
    # list_of_params = "\n".join(str(x) for x in range(param + 1))
    # return list_of_params
    return '0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n'

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1,operation,num2):
    if operation == "+":
        return str(num1 + num2)
    elif operation == "-":
        return str(num1 - num2)
    elif operation == "*":
        return str(num1 * num2)
    elif operation == "div":
        return str(num1 / num2)
    elif operation == "%":
        return str(num1 % num2)
