# Breast Cancer Prediction System 🧬

A simple web application built with Flask to predict whether a tumor is benign or malignant based on 30 input features.

## 🛠 Tech Stack

- Python (Flask)
- HTML, CSS, JavaScript
- scikit-learn (ML model)
- Trained `RandomForestClassifier` model

## 📁 Project Structure

breast-cancer-predictor/ ├── static/ │ ├── style.css │ └── script.js ├── templates/ │ └── index.html ├── model.pkl ├── app.py ├── breast_cancer.csv ├── requirements.txt └── README.md


## 🚀 How to Run

1. Clone this repo or copy files
2. Install dependencies  
   `pip install -r requirements.txt`
3. Run the app  
   `python app.py`
4. Open in browser: `http://localhost:5000`

## 📊 Model Details

- Model: `RandomForestClassifier`
- Trained on: `breast_cancer.csv`
- Accuracy: ~97%

---
