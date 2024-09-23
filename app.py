from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello_world():
    a = 123
    return f'<p>Hello, world!{a}</p>'

@app.route("/login", methods=['POST'])
def login():
    u = request.args.get('user')

    return jsonify({'success': True})
