# Calculator Server(REST API)

from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def operation():
    if request.method == 'GET':
        return (
            "<b>Welcome to the Calculator REST API Server!</b><br><br>"
            "This server does not serve a web page.<br>"
            "To use this API, send a POST request with JSON<br><br>"
            "<b>Supported operations:</b> add, sub, mul, div"
        )
    res = request.get_json()

    op = res['op']
    a = float(res['first'])
    b = float(res['second'])

    match op:
        case "add": ans = f"Addition of two numbers: {a + b}"
        case "sub": ans = f"Subtraction of two numbers: {a - b}"
        case "mul": ans = f"Multiplication of two numbers: {a * b}"
        case "div":
            if b == 0: return jsonify({"error": "Cannot divide by zero!"})
            ans = f"Division of two numbers: {a / b}"
        case _: ans = "Invalid Operator!!"

    return jsonify({"Result": ans})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
