# AI Powered Plagiarism Detection

**"AI-Powered Plagiarism Detection: A Web-Based System for Text Integrity"**

---


# AI-Powered Plagiarism Detection: A Web-Based System for Text Integrity

This repository contains the source code and resources for a web-based plagiarism detection system that leverages AI/ML models to analyze text at the **paragraph level**. It is designed to provide real-time detection using **semantic similarity techniques**, dynamic web querying, and detailed heatmap-based reports.

## Project Highlights

-  **Paragraph-Level Analysis**
-  **Real-Time Web Search via Google APIs**
-  **AI & ML-based Detection using Sentence-BERT**
-  **Similarity Scoring using Cosine Similarity**
-  **Flask Web Interface for Document Uploads**

---

## Paper link

🔗 [IEEE Paper Link](https://ieeexplore.ieee.org/document/11036044)

---

## Tech Stack

| Component         | Technology                         |
|-------------------|------------------------------------|
| Backend           | Python, Flask                      |
| AI Model          | Sentence-BERT, Scikit-learn        |
| Similarity Check  | Cosine Similarity                  |
| Web Search API    | Google Custom Search API           |
| Frontend          | HTML/CSS, Django                   |
| Deployment        | Localhost / Cloud-ready (GCP, AWS) |

---

## Installation & Setup

1. **Clone the Repository**
```
git clone https://github.com/SMVINAYKUMAR2341/AI-Powered-Plagiarism-Detection.git
cd AI-Powered-Plagiarism-Detection
```

2. **Install Dependencies**

```
pip install -r requirements.txt
```

3. **Replace the API keys and search engine ID**<br>
Because this project uses google's search API, it requires an API key and a search engine ID. These are hardcoded in the model itself so we recomend that you add your keys in 'model.py', line 77 & 78.
```
....
results = {}
api_key = # Replace with your API key 
cx = # Replace with your search engine ID

print(f"Total paragraphs: {len(paragraphs)}")
....
```   
5. **Run the App**<br>
Within the folder, open your command prompt/terminal, and run the following:

```
export FLASK_APP=app
flask run
```

5. **Visit**<br>
Click the link that opens up within the browser.
Eg.
```
`http://localhost:5000`
```

---

## Features

* **Upload Text** for checking
* **Paragraph-wise Scores** with matching URLs
* **Open-source and Free to Use**

---

## Citation

If you use this project for academic purposes, please cite the IEEE paper:

> Raghav Purushotham, Rahul Mahato, S.M. Vinay Kumar
> "AI-Powered Plagiarism Detection: A Web-Based System for Text Integrity",
> 2025 IEEE, DOI: [10.1109/11036044](https://ieeexplore.ieee.org/document/11036044)


---

## Acknowledgements

* [IEEE Xplore](https://ieeexplore.ieee.org/)
* [Sentence-BERT by UKP Lab](https://www.sbert.net/)
* [Google Custom Search API](https://programmablesearchengine.google.com/)


