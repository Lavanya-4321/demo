from flask import Flask, request, jsonify, send_file, send_from_directory

import util

app = Flask(__name__)

util.load_saved_artifacts()

@app.route('/')
def home():
    return render_template("index.html")







@app.route('/classify_image', methods=['GET', 'POST'])
def classify_image():
   
    image_data = request.form['image_data']

    response = jsonify(util.classify_image(image_data))

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    
    app.run(host='0.0.0.0', port=10000)
