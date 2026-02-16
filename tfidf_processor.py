from sklearn.feature_extraction.text import TfidfVectorizer

def compute_tfidf(text):
    vectorizer = TfidfVectorizer(
        stop_words='english',
        max_features=1000
    )

    tfidf_matrix = vectorizer.fit_transform([text])
    feature_names = vectorizer.get_feature_names_out()
    scores = tfidf_matrix.toarray()[0]

    term_scores = dict(zip(feature_names, scores))
    return term_scores


def get_top_keywords(term_scores, top_n=10):
    sorted_terms = sorted(term_scores.items(), key=lambda x: x[1], reverse=True)
    return sorted_terms[:top_n]
