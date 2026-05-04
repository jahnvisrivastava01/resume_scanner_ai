# 📄 Resume Scanner AI

## 🌐 Live Demo
Deployed App: https://resume-scanner-ai-1.onrender.com/

---

## 📌 Overview

Resume Scanner AI is a full-stack web application that analyzes uploaded resumes and provides intelligent insights based on selected career roles.

It helps users:
- Evaluate their resume
- Identify missing skills
- Improve job readiness for internships and placements

This project combines:
- 🤖 ML-based role prediction  
- ⚙️ Rule-based skill matching and scoring  

---

## 🚀 Features

### 📂 Resume Upload
- Supports PDF and DOCX files
- Blocks unsupported file types

### 🎯 Role-Based Analysis
- Select a target role
- Compares resume with required skills
- Calculates match score
- Identifies missing skills
- Provides improvement suggestions

### 📊 Smart Output
- Match score with label (Strong / Moderate / Needs Improvement)
- AI predicted role
- Found & missing skills
- Clear recommendations

### 🎨 Web Interface
- Clean and responsive UI
- Fast processing
- Smooth user experience

---

## 🧠 ML Integration

This project uses Machine Learning to enhance resume analysis.

- Uses **TF-IDF Vectorization** for text feature extraction  
- Uses **Multinomial Naive Bayes** for classification  
- Predicts the most suitable job role from resume text  

### Example
```

Resume → "Python, SQL, Data Analysis"
→ Predicted Role: Data Analyst

```

The trained model is stored as `model.pkl`.

---

## 🧰 Tech Stack

### Frontend
- React
- Tailwind CSS
- Vite
- Axios

### Backend
- Python
- FastAPI
- PyPDF2
- python-docx
- scikit-learn

---

## 📂 Project Structure

```

resume-scanner-ai/
│
├── frontend/
│   ├── src/
│   └── package.json
│
├── backend/
│   ├── main.py
│   ├── train_model.py
│   ├── roles.json
│   ├── model.pkl
│   └── utils/
│       ├── parser.py
│       └── matcher.py
│
└── README.md

````

---

## ▶️ Run Locally

### 1️⃣ Clone Repository

```bash
git clone https://github.com/jahnvisrivastava01/resume_scanner_ai.git
cd resume-scanner-ai
````

---

### 2️⃣ Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate   # Windows
pip install fastapi uvicorn python-multipart PyPDF2 python-docx scikit-learn
uvicorn main:app --reload
```

---

### 3️⃣ Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

---

### 4️⃣ Generate ML Model

```bash
cd backend
python train_model.py
```

---

## 📌 Use Cases

* Resume evaluation for students
* Internship & placement preparation
* Skill gap analysis
* Resume improvement tool

---

## 💡 Future Improvements

* AI-powered job description matching
* ATS score calculation
* Resume templates
* User authentication
* Saved history
* Downloadable PDF reports

---

## 👩‍💻 Author

**Jahnvi Srivastava**



