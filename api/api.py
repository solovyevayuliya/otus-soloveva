from flask import Flask, request, jsonify
from core.Interprete import evaluate_expression

app = Flask(__name__)

@app.route('/exec/')
def execute_query():
    query = request.args.get('query')

    try:
        result = evaluate_expression(query)
        status = "valid"
    except SyntaxError:
        result = None
        status = "invalid"

    response = {
        "status": status,
        "result": result
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run()