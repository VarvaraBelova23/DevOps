from flask import Flask, request, jsonify

app = Flask(__name__)

@app.after_request
def add_cors(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    return response

@app.route('/submit', methods=['OPTIONS'])
def submit_options():
    return '', 200

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    text = data.get('text', '')

    with open('data.txt', 'a', encoding='utf-8') as f:
        f.write(text + '\n')

    return jsonify({'status': 'ok', 'received': text})

@app.route('/read', methods=['OPTIONS'])
def read_options():
    return '', 200

@app.route('/read', methods=['GET'])
def read_file():
    try:
        with open('data.txt', 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        content = ''

    return jsonify({'status': 'ok', 'content': content})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)