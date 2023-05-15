from flask import Flask, request, render_template
from chat import generate
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ask/form')
def ask_form():
    return generate(request.form.get("text"))["result"]

@app.route('/ask/render')
def ask_render():
    return render_template("result.html", text=generate(request.args.get("text"))["result"])

@app.route('/ask/args')
def ask_args():
    return generate(request.args.get("text"))["result"]

@app.route('/ask/url/<text>')
def ask_url(text):
    return generate(text)["result"]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
 