from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/products')
def products():
    return jsonify([{"id": 101, "name": "Laptop"}])

app.run(host='0.0.0.0', port=4000)
