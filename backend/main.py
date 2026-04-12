from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

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

# API Route
@app.post("/analyze")
async def analyze(
    file: UploadFile = File(...),
    role: str = Form(...)
):
    resume_text = await extract_text(file)
    result = analyze_resume(resume_text, role)
    return result


# Paths
frontend_path = "../frontend/dist"
assets_path = os.path.join(frontend_path, "assets")
index_file = os.path.join(frontend_path, "index.html")

# Serve assets only if build exists
if os.path.exists(assets_path):
    app.mount("/assets", StaticFiles(directory=assets_path), name="assets")

# Serve React frontend
@app.get("/{full_path:path}")
async def serve_frontend(full_path: str):
    if os.path.exists(index_file):
        return FileResponse(index_file)
    return {"message": "Frontend build not found"}