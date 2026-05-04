import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# ---------------- DATASET ----------------
data = pd.DataFrame({
    "resume_text": [
        "python sql pandas data analysis",
        "html css javascript react frontend",
        "machine learning python tensorflow",
        "java spring boot backend api",
        "react node mongodb full stack",
        "excel sql power bi data visualization"
    ],
    "role": [
        "data analyst",
        "frontend developer",
        "machine learning engineer",
        "backend developer",
        "full stack developer",
        "data analyst"
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