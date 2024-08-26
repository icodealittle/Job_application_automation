# Job Application Automation

This project automates the job application process by collecting job listings from multiple job boards, parsing job descriptions, matching requirements with your resume, generating customized cover letters using OpenAI, submitting applications, and tracking them in a database.

Project structure writes up can be found here: [Automating Job Applications with Artificial Intelligence (AI)](https://www.notion.so/Automating-Job-Applications-with-Artificial-Intelligence-AI-b5a89995b65c4645b7de9404a0c8f4bd?pvs=4)

## Features

- Collect job listings from multiple job boards (e.g., Glassdoor, Indeed, LinkedIn, Monster, CareerBuilder, SimplyHired, ZipRecruiter).
- Parse job descriptions to extract relevant information.
- Match job requirements with your resume.
- Generate customized cover letters using OpenAI's GPT-3.
- Submit job applications.
- Track submitted applications in a SQLite database.

## Project Structure

<pre> 
job_application_automation/
├── config/
│ └── config.yaml
├── data/
│ ├── cover_letters/
│ ├── resumes/
│ └── cover_letter_templates/
├── logs/
│ └── application_automation.log
├── scripts/
│ ├── collect_job_listings.py
│ ├── generate_cover_letter.py
│ └── match_requirements.py
├── .env
├── requirements.txt
└── main.py 
 </pre>

### Conclusion

This README provides a basic overview of the project. Adjust the content as necessary to better fit your specific implementation and preferences.
