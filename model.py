import requests
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import nltk

nltk.download('punkt', quiet=True)


model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

CONFIG = {
    "similarity_threshold": 0.8,  
    "high_similarity_threshold": 0.9,
    "num_api_results": 10,
    "detection_mode": "hybrid",
    "max_retries": 3
}

def calculate_overlap(sentence, snippet):
    sentence_words = set(sentence.lower().split())
    snippet_words = set(snippet.lower().split())
    overlap = sentence_words.intersection(snippet_words)
    return len(overlap) / len(sentence_words) * 100 if sentence_words else 0

def query_web(paragraph, api_key, cx, num_api_results=10, max_retries=3):
    url = "https://www.googleapis.com/customsearch/v1"
    matches = []
    urls = []
    retries = 0

    sentences = nltk.sent_tokenize(paragraph)
    for sentence in sentences:
        if len(sentence) > 2048:
            print(f"Skipping sentence due to length: {sentence}")
            continue

        params = {
            'key': api_key,
            'cx': cx,
            'q': sentence,
            'num': num_api_results
        }

        while retries < max_retries:
            try:
                response = requests.get(url, params=params)
                response.raise_for_status()
                data = response.json()

                for item in data.get('items', []):
                    matches.append(item.get('snippet', ''))
                    urls.append(item.get('link', ''))

                break

            except requests.exceptions.RequestException as e:
                retries += 1
                print(f"Retry {retries}/{max_retries} - Error querying web: {e}")
                if retries == max_retries:
                    print(f"Failed after {max_retries} retries.")

    return matches, urls

def calculate_similarity(sentences, matches):
    sentence_embeddings = model.encode(sentences)
    match_embeddings = model.encode(matches)
    return cosine_similarity(sentence_embeddings, match_embeddings)



def process_text(text, threshold=0.8, detection_mode="hybrid"):
    if not text:
        raise ValueError("Input text cannot be empty or None.")

    paragraphs = text.split('\n\n')
    results = {}
    api_key = "Your_Api_key" 
    cx = "CX API "

    print(f"Total paragraphs: {len(paragraphs)}")

    for para in paragraphs:
        if not para.strip():
            continue

        sentences = nltk.sent_tokenize(para)
        queries = [" ".join(sentences[i:i + 2]) for i in range(0, len(sentences), 2)]

        print(f"Queries for paragraph: {queries}")

        all_matches = []
        all_urls = []

        for query in queries:
            matches, urls = query_web(query, api_key, cx)
            all_matches.extend(matches)
            all_urls.extend(urls)

        if not all_matches:
            results[para] = {"score": 0, "plagiarized_sentences": []}
            continue

        print(f"Snippets fetched: {all_matches}")
        print(f"URLs fetched: {all_urls}")

        similarity_matrix = calculate_similarity(sentences, all_matches)
        print(f"Similarity Matrix: {similarity_matrix}")

        plagiarized_sentences = []
        for i, sentence in enumerate(sentences):
            max_similarity_index = similarity_matrix[i].argmax()
            max_similarity_score = similarity_matrix[i, max_similarity_index]

            if max_similarity_score > threshold:
                overlap = calculate_overlap(sentence, all_matches[max_similarity_index])
                if overlap > 50: 
                    plagiarized_sentences.append({
                        "sentence": sentence,
                        "similarity": round(max_similarity_score * 100, 2),
                        "url": all_urls[max_similarity_index]
                    })

        plagiarism_percentage = len(plagiarized_sentences) / len(sentences) * 100
        results[para] = {
            "score": round(plagiarism_percentage, 2),
            "plagiarized_sentences": plagiarized_sentences
        }

    return results

