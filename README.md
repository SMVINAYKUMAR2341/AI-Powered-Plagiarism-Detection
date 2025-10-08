# AI-Powered-Plagiarism-Detection

**"AI-Powered Plagiarism Detection: A Web-Based System for Text Integrity"**

---

```markdown
# 🧠 AI-Powered Plagiarism Detection: A Web-Based System for Text Integrity

This repository contains the source code and resources for a web-based plagiarism detection system that leverages AI/ML models to analyze text at the **paragraph level**. It is designed to provide real-time detection using **semantic similarity techniques**, dynamic web querying, and detailed heatmap-based reports.

## 🔍 Project Highlights

- ✅ **Paragraph-Level Analysis**
- 🌐 **Real-Time Web Search via APIs**
- 🤖 **AI & ML-based Detection using Sentence-BERT**
- 📊 **Similarity Scoring using Cosine Similarity**
- 📈 **Heatmap Reports & Color-Coded Feedback**
- 📝 **Citation Checking & Recommendations**
- 💻 **Flask Web Interface for Document Uploads**

---

## 🚀 Demo

🔗 [IEEE Paper Link](https://ieeexplore.ieee.org/document/11036044)

---

## 🧰 Tech Stack

| Component         | Technology            |
|------------------|------------------------|
| Backend           | Python, Flask          |
| AI Model          | Sentence-BERT, Scikit-learn |
| Similarity Check  | Cosine Similarity      |
| Web Search API    | Google Custom Search API |
| Frontend          | HTML/CSS, Jinja2       |
| Deployment        | Localhost / Cloud-ready (GCP, AWS) |

---

## 📂 Directory Structure

```

📁 ai-plagiarism-detector
├── app.py                  # Flask backend
├── templates/
│   └── index.html          # Frontend UI
├── static/
│   └── styles.css          # Styling
├── utils/
│   ├── plagiarism\_check.py # Core AI logic
│   └── web\_search.py       # Web query logic
├── models/
│   └── sentence\_bert.pkl   # Serialized ML model
├── requirements.txt        # Python dependencies
└── README.md               # Project info

````

---

## ⚙️ Installation & Setup

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/ai-plagiarism-detector.git
cd ai-plagiarism-detector
````

2. **Install Dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the App**

```bash
python app.py
```

4. **Visit**
   Open your browser and go to `http://localhost:5000`

---

## 📈 Features

* **Upload or Paste Text** for checking
* **Paragraph-wise Scores** with matching URLs
* **Heatmap Visualization** of similarity
* **Exportable Report** with citations and flagged content
* **Open-source and Free to Use**

---

## 📚 Citation

If you use this project for academic purposes, please cite the IEEE paper:

> Raghav Purushotham, Rahul Mahato, S.M. Vinay Kumar
> "AI-Powered Plagiarism Detection: A Web-Based System for Text Integrity",
> 2025 IEEE, DOI: [10.1109/11036044](https://ieeexplore.ieee.org/document/11036044)


---

## ❤️ Acknowledgements

* [IEEE Xplore](https://ieeexplore.ieee.org/)
* [Sentence-BERT by UKP Lab](https://www.sbert.net/)
* [Google Custom Search API](https://programmablesearchengine.google.com/)



---

Let me know if you'd like this in `.md` file format directly or want me to help create `requirements.txt`, a sample Flask structure, or deployment guide too.
```
