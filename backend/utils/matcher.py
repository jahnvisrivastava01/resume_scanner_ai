import json
import pickle
import os

# ---------------- PATH SETUP ----------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")
ROLES_PATH = os.path.join(BASE_DIR, "roles.json")

# ---------------- LOAD MODEL ----------------
try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
except Exception as e:
    model = None
    print("⚠️ Model load error:", e)


# ---------------- MAIN FUNCTION ----------------
def analyze_resume(resume_text, role):

    # ----------- SAFETY CHECK -----------
    if not resume_text:
        return {"error": "No resume text provided"}

    resume_text_lower = resume_text.lower()

    # ----------- ML PREDICTION -----------
    if model:
        try:
            predicted_role = model.predict([resume_text])[0]
        except Exception:
            predicted_role = "Unknown"
    else:
        predicted_role = "Model not available"

    # ----------- LOAD ROLES -----------
    try:
        with open(ROLES_PATH, "r") as file:
            roles = json.load(file)
    except Exception as e:
        return {"error": f"roles.json error: {str(e)}"}

    # ----------- FIX ROLE MATCHING -----------
    role_key = role.strip().lower()

    if role_key not in roles:
        return {
            "error": f"Role '{role}' not found",
            "available_roles": list(roles.keys())
        }

    required_skills = roles.get(role_key, [])

    # ----------- SKILL MATCHING (IMPROVED) -----------
    found_skills = []
    missing_skills = []

    for skill in required_skills:
        skill_lower = skill.lower()

        # Match any word inside skill
        if any(word in resume_text_lower for word in skill_lower.split()):
            found_skills.append(skill)
        else:
            missing_skills.append(skill)

    # ----------- SCORE CALCULATION -----------
    if required_skills:
        score = int((len(found_skills) / len(required_skills)) * 100)
    else:
        score = 0

    # ----------- SMART SUGGESTION -----------
    if score >= 70:
        suggestion = "Great! Your resume matches the role well."
    elif missing_skills:
        suggestion = "Improve your resume by adding: " + ", ".join(missing_skills)
    else:
        suggestion = "Resume needs improvement."

    # ----------- FINAL RESPONSE -----------
    return {
        "predicted_role": predicted_role,   # ML Output
        "target_role": role,
        "match_score": score,
        "found_skills": found_skills,
        "missing_skills": missing_skills,
        "suggestion": suggestion
    }