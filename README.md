# AI Resume Analyzer

An intelligent tool designed to parse resumes and score them against job descriptions to help candidates optimize their applications for Applicant Tracking Systems (ATS).

## Project Structure (as seen in image_0cd956.png)
- `parser.py`: Extracts text and key entities from resumes.
- `scorer.py`: Analyzes the resume against job requirements to provide a relevance score.
- `job_search.py`: Module to pull relevant job data for comparison.
- `endpoints.py`: API layer to handle user requests.
- `index.html`: The frontend interface for user interaction.

## How it works
1. **Upload**: User uploads a resume and pastes a job description.
2. **Analyze**: `parser.py` extracts skills and experience.
3. **Score**: `scorer.py` evaluates the match percentage.
4. **Improve**: Receive actionable feedback to boost the resume's ATS ranking.
