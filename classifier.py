from transformers import pipeline

# Initialize pipeline
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

CANDIDATE_LABELS = [
    "This document is an invoice",
    "This document is a resume",
    "This document is a scientific paper",
    "This document is an email",
    "This document is a project report"
]

def classify_document(text):
    # truncate long text
    text = " ".join(text.split()[:1000])

    # classify
    result = classifier(text, CANDIDATE_LABELS, multi_label=False)

    # some versions return a list
    if isinstance(result, list):
        result = result[0]

    # return a dict, not just a string
    return {
        "category": result["labels"][0],
        "confidence": float(result["scores"][0]),
        "all_scores": dict(zip(result["labels"], result["scores"]))
    }
