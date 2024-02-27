from flask import Flask, request, jsonify, send_file, render_template
from tensorflow.keras.models import load_model
import tensorflow as tf
import cv2
import numpy as np
import os
import zipfile
import tempfile

app = Flask(__name__, template_folder='template', static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download_model')
def download_model():
    return send_file('model_savemodel.zip', as_attachment=True)

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        model_dir = 'pothole/model_savemodel'  # Path to the model directory
        model = load_model('C:/Users/shash/Desktop/POTHOLE/model_savemodel')

        file = request.files['image']
        if file:
            img = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
            img = cv2.resize(img, (128, 128))
            img = img / 255.0
            img = np.expand_dims(img, axis=0)
            prediction = model.predict(img)
            try:
                output = prediction[0]  # Assuming the output is a single value
                prediction_number = float(output[0])
                prediction_label = "Pothole" if prediction_number > 0.5 else "No Pothole"
                return jsonify({'prediction': prediction_number, 'label': prediction_label})
            except IndexError:
                return jsonify({'error': 'Output index out of range'})
        else:
            return jsonify({'error': 'No file uploaded'})
    else:
        return jsonify({'error': 'Method not allowed'})


if __name__ == '__main__':
    app.run(debug=True)
