from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse # Moved to top
import uvicorn
import os
import sys

# Ensure local imports work regardless of folder depth
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.parser import extract_text_from_pdf
from core.scorer import get_match_report, extract_missing_skills

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "Online", "message": "AI Resume Analyzer Backend is Running Successfully!"}

@app.post("/analyze")
async def analyze_resume(resume: UploadFile = File(...), job_description: str = Form(...)):
    try:
        # Save file temporarily
        temp_path = f"temp_{resume.filename}"
        with open(temp_path, "wb") as buffer:
            buffer.write(await resume.read())

        # Process
        text = extract_text_from_pdf(temp_path)
        score = get_match_report(text, job_description)
        missing = extract_missing_skills(text, job_description)

        # Cleanup
        os.remove(temp_path)

        return {
            "status": "success",
            "match_score": score,
            "missing_skills": missing
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

# Moved this route outside the main block so FastAPI can see it
@app.post("/download-optimized")
async def download_optimized(role: str = Form(...), skills: str = Form(...)):
    # Create a professional "Strong" resume content
    content = f"""
PROFESSIONAL SUMMARY
Results-driven {role} with a strong foundation in modern software development. 
Highly proficient in {skills}, with a proven track record of optimizing system 
performance and delivering scalable solutions. 

CORE COMPETENCIES
* Technical Leadership & Strategy
* {skills.replace(',', '\n* ')}
* Problem Solving & Analytical Thinking

EXPERIENCE & PROJECTS
Implemented high-end solutions using {skills.split(',')[0] if skills else 'core technologies'} 
to enhance operational efficiency and maintain high code quality standards.
    """
    
    file_path = "Optimized_Resume_Draft.txt"
    with open(file_path, "w") as f:
        f.write(content.strip())
        
    return FileResponse(file_path, filename=f"Optimized_{role.replace(' ', '_')}_Resume.txt")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)