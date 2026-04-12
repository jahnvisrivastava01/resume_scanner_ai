# 🚀 Resume Scanner AI – Role Readiness Analyzer

## 📌 Overview

Resume Scanner AI is a smart web application that helps users evaluate how well their resume matches a target career role.

Users can upload their resume, select a job role, and receive instant feedback based on the skills required for that role.

The system analyzes the resume and provides:

- 📊 Match Score  
- ✅ Found Skills  
- ❌ Missing Skills  
- 💡 Personalized Suggestions  

This project is useful for students, freshers, and job seekers who want to improve their resume before applying for jobs.

---

# ✨ Features

## 📄 Resume Upload
- Upload PDF or DOCX resume files
- Automatically extracts text from resume

## 🎯 Role-Based Analysis
Choose a target role and compare your resume with required skills.

Supported roles:

- Frontend Developer
- Backend Developer
- Full Stack Developer
- Python Developer
- Java Developer
- Data Analyst
- Machine Learning Engineer
- UI/UX Designer
- Android Developer
- Software Tester
- DevOps Engineer
- General Fresher

## 📊 Smart Insights
After analysis, users get:

- Resume Match Percentage
- Skills Found in Resume
- Missing Skills to Learn
- Suggestions to Improve Resume

## 🎨 Modern UI
- Responsive design
- Clean dashboard
- Tailwind CSS styling
- Easy to use interface

---

# 🧠 Tech Stack

## Frontend
- React.js
- Vite
- Tailwind CSS
- Axios

## Backend
- Python
- FastAPI
- PyPDF2
- python-docx

## Tools
- GitHub
- Vercel (Frontend Deployment)
- Render (Backend Deployment)

---

# 📂 Project Structure

```bash
resume-scanner-ai/
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── backend/
│   ├── main.py
│   ├── roles.json
│   └── utils/
│       ├── parser.py
│       └── matcher.py
│
└── README.md
---

##⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/yourusername/resume-scanner-ai.git
cd resume-scanner-ai
▶️ Run Frontend
Open terminal 1:

cd frontend
npm install
npm run dev

Frontend runs on:
http://localhost:5173

▶️ Run Backend
Open terminal 2:

cd backend
python -m venv venv
source venv/Scripts/activate
pip install fastapi uvicorn python-multipart PyPDF2 python-docx
uvicorn main:app --reload

Backend runs on:
http://127.0.0.1:8000
---
🔄 How Frontend & Backend Work Together
User opens frontend in browser
Uploads resume file
Selects target role
React sends request to FastAPI backend
Backend reads resume text
Skills are compared with selected role
Result is sent back to frontend
UI displays score, missing skills, and suggestions
---
🧠 How It Works Internally
Backend Modules
parser.py
Reads PDF / DOCX files
Extracts text content from resume
matcher.py
Loads role skills from roles.json
Checks which skills are present
Calculates match score
Generates suggestions
main.py
Creates FastAPI server
Handles API requests
Returns JSON response
---
📊 Example Output
Input:
Resume uploaded
Selected Role: Frontend Developer
Result:
Match Score: 75%
Found Skills: HTML, CSS, JavaScript, React
Missing Skills: Git, API
Suggestion: Add projects using Git and API integration
---
🚀 Future Improvements
🤖 AI-powered resume feedback using OpenAI API
📄 ATS Resume Score Checker
📝 Cover Letter Generator
📥 Download PDF Report
🔐 User Login / Signup System
💾 Save Previous Resume Scans
🎯 Drag & Drop Resume Upload
🌙 Dark / Light Mode
📊 Resume Analytics Dashboard
🌍 Multi-language Support
📱 Better Mobile Experience
☁️ Cloud Deployment with CI/CD
🎯 Why This Project Matters
---
##This project solves a real-world problem for:

🎓 Students preparing for placements
👩‍💻 Freshers applying for jobs
🔄 Career switchers
🚀 Professionals improving resumes
---

👩‍💻 Author
Jahnvi Srivastava
