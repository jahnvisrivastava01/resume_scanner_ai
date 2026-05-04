import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# ---------------- DATASET ----------------
data = pd.DataFrame({
    "resume_text": [
        # Data Analyst
        "python sql pandas excel data analysis power bi tableau",
        "data cleaning visualization statistics sql python",

        # Frontend
        "html css javascript react tailwind frontend ui",
        "react js responsive design api integration html css",

        # Backend
        "node js express mongodb api backend development",
        "java spring boot rest api sql backend",

        # Full Stack
        "react node mongodb full stack development api",
        "html css javascript node express full stack",

        # ML Engineer
        "machine learning python tensorflow numpy pandas",
        "deep learning nlp python scikit learn",

        # Tester
        "manual testing selenium test cases bug tracking jira",
        "automation testing selenium webdriver qa testing",

        # DevOps
        "docker kubernetes aws linux ci cd jenkins",
        "devops pipelines cloud deployment docker kubernetes"
    ],
    "role": [
        "data analyst","data analyst",
        "frontend developer","frontend developer",
        "backend developer","backend developer",
        "full stack developer","full stack developer",
        "machine learning engineer","machine learning engineer",
        "software tester","software tester",
        "devops engineer","devops engineer"
    ]
})

X = data["resume_text"]
y = data["role"]

# ---------------- MODEL ----------------
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", MultinomialNB())
])

# Train model
model.fit(X, y)

# ---------------- SAVE MODEL ----------------
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ model.pkl successfully created!")