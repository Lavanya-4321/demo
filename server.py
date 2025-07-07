from flask import Flask, request, jsonify, send_file, send_from_directory

import util

app = Flask(__name__)
@app.route('/')
def home():
    return send_file("app.html")

@app.route('/app.css')
def serve_css():
    return send_from_directory('.', 'app.css')
@app.route('/app.js')
def serve_js():
    return send_from_directory('.', 'app.js')





@app.route('/classify_image', methods=['GET', 'POST'])
def classify_image():
    util.load_saved_artifacts()
    image_data = request.form['image_data']

    response = jsonify(util.classify_image(image_data))

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    
    app.run(port=5000)
