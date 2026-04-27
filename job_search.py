import urllib.parse

def get_job_links(role, location="India"):
    # High-end approach: Generate dynamic search URLs for the user
    query = urllib.parse.quote(f"{role} jobs in {location}")
    
    links = {
        "LinkedIn": f"https://www.linkedin.com/jobs/search/?keywords={query}",
        "Naukri": f"https://www.naukri.com/{role.replace(' ', '-')}-jobs-in-{location}",
    }
    return links