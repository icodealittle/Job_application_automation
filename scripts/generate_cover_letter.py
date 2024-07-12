import openai
import yaml
from dotenv import load_dotenv
import os
import time

# Load environment variables from .env file
load_dotenv()

# Ensure the API key is loaded correctly
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise ValueError(
        "OpenAI API key not set. Please set the OPENAI_API_KEY environment variable."
    )


def generate_cover_letter(job, role):
    with open(
        "config/config.yaml", "r"
    ) as file:
        config = yaml.safe_load(file)

    cover_letter_template_path = config["cover_letter_templates"][role]
    with open(cover_letter_template_path, "r") as file:
        cover_letter_template = file.read()

    job_details = {
        "company": job["company"],
        "title": job["title"],
        "skills": job["matched_skills_resume"],
    }

    cover_letter = cover_letter_template.format(
        title=job_details["title"],
        company=job_details["company"],
        skills=", ".join(job_details["skills"]),
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # or use "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": cover_letter},
            ],
            max_tokens=500,
            n=1,
            stop=None,
            temperature=0.7,
        )
        generated_cover_letter = response["choices"][0]["message"]["content"].strip()
    except openai.error.RateLimitError as e:
        print(f"Rate limit exceeded: {e}")
        print("Waiting for 60 seconds before retrying...")
        time.sleep(60)  # Wait for 60 seconds before retrying
        return generate_cover_letter(job, role)

    cover_letter_path = f"data/cover_letters/cover_letter_{job_details['company']}_{job_details['title']}_{role}.txt"
    with open(cover_letter_path, "w") as file:
        file.write(generated_cover_letter)

    job["cover_letter_path"] = cover_letter_path
    return job


if __name__ == "__main__":
    job = {
        "company": "Example Corp",
        "title": "Data Scientist",
        "matched_skills_resume": ["Python", "SQL", "machine learning"]
    }
    updated_job = generate_cover_letter(job, "data_scientist")
    print(updated_job)

# import openai
# import yaml
# from dotenv import load_dotenv
# import os
# import time

# load_dotenv()

# openai.api_key = os.getenv("OPENAI_API_KEY")
# if not openai.api_key:
#     raise ValueError(
#         "OpenAI API key not set. Please set the OPENAI_API_KEY environment variable."
#     )

# def generate_cover_letter(job, role):
#     with open("config/config.yaml", "r") as file:
#         config = yaml.safe_load(file)

#     cover_letter_template_path = config["cover_letter_templates"][role]
#     with open(cover_letter_template_path, "r") as file:
#         cover_letter_template = file.read()

#     job_details = {
#         'company': job['company'],
#         'title': job["title"],
#         "skills": job['matched_skills_resume']
#     }

#     cover_letter = cover_letter_template.format(
#         title = job_details['title'],
#         company = job_details['company'],
#         skills = ", ".join(job_details['skills'])
#     )

#     # openai.api_key = os.getenv("OPENAI_API_KEY")

#     # response = openai.ChatCompletion.create(
#     #     model="gpt-4",
#     #     messages=[
#     #         {"role": "system", "content": "You are a helpful assistant."},
#     #         {"role": "user", "content": cover_letter}
#     #     ],
#     #     max_tokens=500,
#     #     n=1,
#     #     stop=None,
#     #     temperature=0.7,
#     # )

#     # response = openai.Completion.create(
#     #     engine="text-davinci-003",  # GPT-3 model
#     #     prompt=cover_letter,
#     #     max_tokens=500,
#     #     n=1,
#     #     stop=None,
#     #     temperature=0.7,
#     # )

#     # response = openai.ChatCompletion.create(
#     #     model="gpt-3.5-turbo",  # or use "gpt-4" if you have access
#     #     messages=[
#     #         {"role": "system", "content": "You are a helpful assistant."},
#     #         {"role": "user", "content": cover_letter}
#     #     ],
#     #     max_tokens=500,
#     #     n=1,
#     #     stop=None,
#     #     temperature=0.7,
#     # )

#     # generated_cover_letter = response["choices"][0]["message"]["content"].strip()

#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",  # or use "gpt-4" if you have access
#             messages=[
#                 {"role": "system", "content": "You are a helpful assistant."},
#                 {"role": "user", "content": cover_letter},
#             ],
#             max_tokens=500,
#             n=1,
#             stop=None,
#             temperature=0.7,
#         )
#         generated_cover_letter = response["choices"][0]["message"]["content"].strip()
#     except openai.error.RateLimitError as e:
#         print(f"Rate limit exceeded: {e}")
#         print("Waiting for 60 seconds before retrying...")
#         time.sleep(60)  # Wait for 60 seconds before retrying
#         return generate_cover_letter(job, role)

#     cover_letter_path = f"data/cover_letters/cover_letter_{job_details['company']}_{job_details['title']}_{role}.txt"
#     with open(cover_letter_path, 'w') as file:
#         file.write(generated_cover_letter)

#     job["cover_letter_path"] = cover_letter_path
#     return job

# if __name__ == "__main__":

#     job = {
#         "company": "Example Corp",
#         "title": "Data Scientist",
#         "matched_skills_resume": ["Python", "SQL", "machine learning"],
#     }
#     updated_job = generate_cover_letter(job, "data_scientist")
#     print(updated_job)
