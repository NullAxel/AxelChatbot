from flask import Flask, render_template
from chat import generate
app = Flask(__name__)

@app.route('/ask/form')
def ask_form():
    return generate(request.form.get("text"))

@app.route('/ask/args')
def ask_args():
    return generate(request.args.get("text"))

@app.route('/ask/url/<text>')
def ask_args(text):
    return generate(text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
 