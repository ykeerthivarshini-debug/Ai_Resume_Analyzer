import re
from sentence_transformers import SentenceTransformer, util

# Load the model once when the server starts
# This handles the "AI" part of your project without needing an API key
model = SentenceTransformer('all-MiniLM-L6-v2')

# High-End Tech Keyword Library
TECH_KEYWORDS = [
    "python", "java", "javascript", "c++", "c#", "ruby", "php", "go", "rust", "swift", "kotlin", "typescript",
    "html", "css", "react", "angular", "vue", "node.js", "express", "django", "flask", "fastapi", "spring boot",
    "machine learning", "deep learning", "nlp", "tensorflow", "pytorch", "scikit-learn", "pandas", "numpy",
    "sql", "mysql", "postgresql", "mongodb", "redis", "nosql", "firebase", "aws", "azure", "gcp", "docker", 
    "kubernetes", "jenkins", "git", "github", "cicd", "rest api", "graphql", "tableau", "power bi", "linux"
]

def get_match_report(resume_text, job_description):
    """Calculates Semantic Similarity Score."""
    if not resume_text or not job_description:
        return 0
    
    emb1 = model.encode(resume_text, convert_to_tensor=True)
    emb2 = model.encode(job_description, convert_to_tensor=True)
    
    cosine_scores = util.cos_sim(emb1, emb2)
    score = float(cosine_scores[0][0]) * 100
    return round(max(0, min(100, score)), 1)

def extract_missing_skills(resume_text, jd_text):
    """Finds JD keywords missing from the Resume."""
    resume_text = resume_text.lower()
    jd_text = jd_text.lower()
    
    # Identify skills present in JD
    jd_skills = {skill for skill in TECH_KEYWORDS if re.search(rf"\b{re.escape(skill)}\b", jd_text)}
    # Identify skills present in Resume
    resume_skills = {skill for skill in TECH_KEYWORDS if re.search(rf"\b{re.escape(skill)}\b", resume_text)}
    
    # Missing = In JD but NOT in Resume
    missing = jd_skills - resume_skills
    return sorted(list(missing))