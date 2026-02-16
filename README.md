# PDF Document Classifier
## 📌 Project Overview

This project classifies text-based PDF documents into predefined categories using Machine Learning (Zero-Shot Transformer model).

The system:
  1. Extracts text from PDF files
  2. Classifies the document
  3. Returns predicted category
  4. Displays confidence score
## 🎯Supported Document Categories

* Invoice

* Resume

* Scientific Document

* Email

* Project Report
## 🧠 Technologies Used

- Python 3.11

- Hugging Face Transformers

- Zero-Shot Classification

- PyPDF / PDF text extraction

- Virtual Environment (venv)
## 📂 Pdf_Document_Classifier_AWS/
PDF_AUTOMATION_PROJECT/

├── pdfs/                       # Sample input PDF files

│    └── Email_Document.pdf

│    └── Invoice.pdf

│    └── Project Report.pdf

│    └── Resume.pdf

│    └── Scientific_Document.pdf

├── classifier.py              # Document classification logic

├── extractor.py               # PDF text extraction

├── metadata.py                # Metadata extraction

├── tfidf_processor.py         # TF-IDF keyword extraction

├── storage.py                 # Output storage handling

├── main.py                    # Main execution script
│

├── output.json                # Sample output result

├── .gitignore

  └── README.md

## 🏗 Architecture Diagram

<img width="933" height="317" alt="image" src="https://github.com/user-attachments/assets/a95b72bf-541f-42bf-8d3b-84247b343ce6" />

## ⚙️ Installation & Setup

### 1. Clone the repository
  * git clone https://github.com/alimirza817/Pdf_Document_Classifier_AWS.git
  * cd Pdf_Document_Classifier_AWS
### 2. Create virtual environment
  * python -m venv venv
Activate it:
#### Windows:
  * venv\Scripts\activate
#### Mac/Linux:
  * source venv/bin/activate
### 3. Install dependencies
  * pip install -r requirements.txt
## ▶️ How to Run
  * python main.py
  * The system will:

1. Read the PDF

2. Extract text

3. Apply Zero-Shot Transformer

4. Print predicted category with confidence score
## 📊 Example Output
  * Processing: Invoice.pdf
  
  * Predicted Category: Invoice
  
  * Confidence Score: 0.94
## Screenshots
### 1. Project Structure (VS Code Explorer)
   <img width="1351" height="718" alt="image" src="https://github.com/user-attachments/assets/9eab5a69-97a0-4a8b-9fae-a3458cb9be5d" />
   
### 2. Terminal Execution
   <img width="1011" height="311" alt="image" src="https://github.com/user-attachments/assets/86040654-732a-4850-b659-c539535e8ea3" />
   
### 3. Json Output
   <img width="1001" height="390" alt="image" src="https://github.com/user-attachments/assets/5950269c-b609-4ace-8330-bd61c8783ae1" />
   
## 🔍 How It Works

1. Extract text from PDF

2. Pass extracted text to Zero-Shot Transformer model

3. Compare text against predefined labels

4. Return highest probability label
## 🚀 Future Improvements

* AWS Lambda deployment

* API endpoint integration

* Web interface (Flask/FastAPI)

* Vector database support

* Batch processing support
 

