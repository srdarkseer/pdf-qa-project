import os
from flask import Flask, request, jsonify
from pdf_extractor import extract_text_from_pdf
from qa_model import load_model, answer_query

app = Flask(__name__)
nlp = load_model()  # Load the model when starting the app

# Temporary storage for text extracted from the uploaded PDF
pdf_text = ""

@app.route('/upload', methods=['POST'])
def upload_file():
    global pdf_text
    pdf = request.files['file']
    upload_folder = 'uploads'
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)  # Create the directory if it does not exist
    pdf_path = os.path.join(upload_folder, pdf.filename)
    pdf.save(pdf_path)
    pdf_text = extract_text_from_pdf(pdf_path)
    return jsonify({"message": "PDF uploaded and processed successfully"})

@app.route('/query', methods=['GET'])
def query_pdf():
    question = request.args.get('question')
    if not question or not pdf_text:
        return jsonify({"answer": "No query provided or PDF not uploaded"})
    answer = answer_query(question, pdf_text, nlp)
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)
