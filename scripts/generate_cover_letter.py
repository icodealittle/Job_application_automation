import openai
import yaml
from dotenv import load_dotenv
import os

load_dotenv()

def generate_cover_letter(job, role):
    with open("config/config.yaml", "r") as file:
        config = yaml.safe_load(file)