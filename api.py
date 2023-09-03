from core.Interprete import evaluate_expression
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    query = request.form['text'].upper()
    processed_text = evaluate_expression(query)
    return str(processed_text)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
