import json
import pickle
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")
ROLES_PATH = os.path.join(BASE_DIR, "roles.json")

# Load ML model
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)


def analyze_resume(resume_text, role):

    if not resume_text:
        return {"error": "No resume text provided"}

    resume_text_lower = resume_text.lower()

    # 🔥 ML Prediction
    predicted_role = model.predict([resume_text])[0]

    # Load roles
    with open(ROLES_PATH, "r") as file:
        roles = json.load(file)

    role_key = role.strip().lower()
    required_skills = roles.get(role_key, [])

    found_skills = []
    missing_skills = []

    for skill in required_skills:
        if skill.lower() in resume_text_lower:
            found_skills.append(skill)
        else:
            missing_skills.append(skill)

    score = int((len(found_skills) / len(required_skills)) * 100) if required_skills else 0

    if score >= 70:
        suggestion = "Great! Your resume matches the role well."
    else:
        suggestion = "Improve your resume by adding: " + ", ".join(missing_skills)

    return {
        "predicted_role": predicted_role,   # 🔥 IMPORTANT
        "target_role": role,
        "match_score": score,
        "found_skills": found_skills,
        "missing_skills": missing_skills,
        "suggestion": suggestion
    }