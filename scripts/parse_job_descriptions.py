import spacy
import re
import yaml
import os

nlp = spacy.load('en_core_web_sm')

def extract_experience(job_description, keywords):
    for keyword in keywords:
        match = re.search(rf"(\d+)\s+{keywords}", job_description, re.IGNORECASE)
        if match:
            return int(match.group(1))
    return None

def parse_job_description(job, role, config):
    job_description = job['description']
    doc - nlp(job_description)
    
    role_config = config['roles'][role]
    skills = role_config['skills']
    keywords = role_config['keywords']
    matched_skills = [skill for skill in skills if skill.lower() in job_description.lower()]
    matched_keywords = [keyword for keyword in keywords if keyword.lower() in job_description.lower()]
    
    responsibility = []
    
    for sent in doc.sents:
        # TODO: Figure out how to finish this for loops and what to return here

        if "...." in send.text.lower():
            responsibility.append(sent.text.strip())
    Exp_keywords = 

        
