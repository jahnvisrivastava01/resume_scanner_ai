import json

def analyze_resume(resume_text, role):

    with open("roles.json", "r") as file:
        roles = json.load(file)

    required_skills = roles.get(role.lower(), [])

    found_skills = []
    missing_skills = []

    for skill in required_skills:
        if skill in resume_text:
            found_skills.append(skill)
        else:
            missing_skills.append(skill)

    score = int((len(found_skills) / len(required_skills)) * 100) if required_skills else 0

    return {
        "role": role,
        "match_score": score,
        "found_skills": found_skills,
        "missing_skills": missing_skills,
        "suggestion": f"Add projects or experience using: {', '.join(missing_skills)}"
    }