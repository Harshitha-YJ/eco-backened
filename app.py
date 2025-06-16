from flask import Flask, request, jsonify
from flask_cors import CORS
from scripts.data_extractor import BiomarkerExtractor
import os

app = Flask(__name__)           # ✅ Define app first
CORS(app)                       # ✅ Now this line is safe
extractor = BiomarkerExtractor()

@app.route('/')
def home():
    return "EcoTown Health Backend is running."

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    # Process it and return a response
    return jsonify({"message": "Upload received", "filename": file.filename})

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
