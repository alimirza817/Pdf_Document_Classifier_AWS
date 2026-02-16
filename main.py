import os
from extractor import extract_text
from tfidf_processor import compute_tfidf, get_top_keywords
from metadata import extract_metadata
from storage import save_document
from classifier import classify_document

PDF_FOLDER = "pdfs"

for file in os.listdir(PDF_FOLDER):
    if file.endswith(".pdf"):
        path = os.path.join(PDF_FOLDER, file)

        print(f"Processing {file}...")

        text = extract_text(path)

        # Classification Step
        prediction = classify_document(text)
        category = prediction["category"]
        confidence = prediction["confidence"]

        # TF-IDF Processing
        term_scores = compute_tfidf(text)
        top_keywords = get_top_keywords(term_scores)

        # Metadata Extraction
        metadata = extract_metadata(text, category)

        record = {
            "filename": file,
            "category": category,
            "confidence": round(confidence, 4),
            "top_keywords": top_keywords,
            "metadata": metadata
        }

        save_document(record)

        print(f"Finished {file}\n")
