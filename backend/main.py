from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware

from utils.parser import extract_text
from utils.matcher import analyze_resume

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Resume Scanner API Running"}

@app.post("/analyze")
async def analyze(
    file: UploadFile = File(...),
    role: str = Form(...)
):
    resume_text = await extract_text(file)
    result = analyze_resume(resume_text, role)
    return result