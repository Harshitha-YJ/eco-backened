from flask import Flask, request, jsonify
from scripts.data_extractor import BiomarkerExtractor 
import os

app = Flask(__name__)
extractor = BiomarkerExtractor()

@app.route('/')
def home():
    return "EcoTown Health Backend is running."

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    if file.filename.endswith('.pdf'):
        data = extractor.extract_from_pdf(file.stream)
    elif file.filename.endswith('.csv'):
        data = extractor.extract_from_csv(file.stream)
    else:
        return jsonify({"error": "Unsupported file type"}), 400

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
