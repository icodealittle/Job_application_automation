import spacy
import PyPDF2
import yaml
from dotenv import load_dotenv
import os

load_dotenv()

nlp = spacy.load("en_core_web_sm")


def extract_text_from_pdf(file_path):

    pdf_reader = PyPDF2.PdfFileReader(file_path)
    text = ""

    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        text += page.extract_text()
    return text


def match_requirements(job, role, config):
    resume_path = config["resume_path"][role]
    resume_text = extract_text_from_pdf(resume_path)
    resume_nlp = nlp(resume_text)

    job_skills = job["matched_skills"]
    resume_skills = [ent.text for ent in resume_nlp.ents if ent.label_ == "SKILL"]
    matched_skills_resume = [skill for skill in job_skills if skill in resume_skills]

    job["matched_skills_resume"] = matched_skills_resume

    return job
