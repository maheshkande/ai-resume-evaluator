from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(resume_text, job_description):
    try:
        documents = [resume_text, job_description]

        tfidf = TfidfVectorizer().fit_transform(documents)
        similarity_matrix = cosine_similarity(tfidf[0:1], tfidf)

        similarity_score = round(similarity_matrix[0][1] * 100, 2)
        return similarity_score
    except Exception as e:
        return f"Error during similarity calculation: {e}"
