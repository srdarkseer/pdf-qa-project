# PDF Question Answering Flask Application
<br>

This project is a Flask-based web application that allows users to upload PDF documents and ask questions based on the content of the PDFs. The application uses a pre-trained NLP model from the `transformers` library to extract answers from the text of the PDFs.
<br>
<br>

## **Features**

- **PDF Upload**: Users can upload PDF documents to the server.
- **Question Answering**: Users can ask questions about the content of the uploaded PDFs, and the system will return answers extracted from the text.
<br>
<br>

## **Installation**

To set up and run this project locally, follow these steps:

### Prerequisites

- Python 3.8 or higher
- pip
<br>
<br>

## **Setup**

1. **Clone the repository**:

```bash
git clone https://github.com/srdarkseer/pdf-qa-project.git
cd pdf-qa-project
```
<br>

2. **Create a virtual environment**:

```bash
python -m venv venv
source venv/bin/activate # On Windows use venv\Scripts\activate
```
<br>

3. **Install the required dependencies**:

```bash
pip install -r requirements.txt
```
<br>

### Running the Application

1. **Start the Flask application**:

```bash
python app.py
```
<br>

2. **Accessing the Server**:

The server will start on http://127.0.0.1:5000. You can access the endpoints via a web browser or tools like Postman or curl.
<br>
<br>

## **Usage**
<br>

**Uploading a PDF**

- **Endpoint**: `/upload`
- **Method**: POST
- **Body**: Multipart/form-data with a file field
<br>
<br>

**Example using curl**:

```bash
curl -X POST -F 'file=@/path/to/your/pdf.pdf' http://127.0.0.1:5000/upload
```
<br>

**Asking a Question**

- **Endpoint**: `/query`
- **Method**: GET
- **Query Parameter**: `question`

```bash
curl "http://127.0.0.1:5000/query?question=What is the main topic of the document?"
```
<br>

## **Contributing**

Contributions are welcome! Please feel free to submit a pull request.

## **Acknowledgments**

- Hugging Face for the `transformers` library.
- PyMuPDF for PDF text extraction functionalities.

### **Additional Notes:**

- **Customization**: Adjust the repository URL (`https://github.com/yourusername/pdf-qa-project.git`) to your actual GitHub repository URL.
- **Formatting and Structure**: This Markdown format is designed to be easy to read and navigate, providing a clear guide to using and contributing to your project.
- **Details and Expansion**: You might want to expand the **Installation** section to include more specific details about setting up the environment or handling potential errors during setup.
<br>
<br>
----
# Thank You!
