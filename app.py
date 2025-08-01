from flask import Flask, render_template, request
from model import process_text  #
from config import CONFIG


"""

DO NOT FORGET TO USE THESE COMMANDS TO RUN THE FILES 

source venv/bin/activate
export FLASK_APP=app
flask run

"""


app = Flask(__name__)

CONFIG = {
    "similarity_threshold": 0.6,
    "high_similarity_threshold": 0.8,
    "relaxed_similarity_threshold": 0.4,
    "num_api_results": 10,
    "detection_mode": "hybrid",
    "max_retries": 3
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
@app.route('/analyze', methods=['POST'])
def analyze():
    if 'file' not in request.files:
        return "No file uploaded", 400

    file = request.files['file']
    text = file.read().decode('utf-8')

    detection_mode = "hybrid"  
    threshold = 0.6  

    try:
        results = process_text(text, threshold=threshold, detection_mode=detection_mode)
        print(f"Results: {results}")  # Debug: Print results
    except Exception as e:
        print(f"Error processing text: {e}")
        return "An error occurred during processing", 500

    total_score = sum(result["score"] for result in results.values())
    average_score = round(total_score / len(results), 2) if results else 0
    print(f"Average Score: {average_score}")  # Debug: Print average score

    return render_template('results.html', results=results, average_score=average_score)

if __name__ == '__main__':
    app.run(debug=True)

