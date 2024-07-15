from playwright.sync_api import sync_playwright
import yaml

def collect_job_listings(config):
    
    jobs = []
    
    def run(playwright):
        
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        
        for job_board in config['job_boards']:
            page.goto(job_board['url'])
            page.wait_for_job_selector(f'.{job_board['listing_class']}', timeout = 10000)
            
            job_elements = page.query_selector_all(f'.{job_board['listing_class']}')
            for job_element in job_elements:
                try:
                    title = job_element.query_selector(f'.{job_board['title_tag']}').inner_text()
                    company = job_element.query_selector(f'.{job_board['company_class']}').inner_text()
                    location = job_element.query_selector(f'.{job_board['location_class']}').inner_text()
                    description = job_element.query_selector(f'.{job_board['description_class']}').inner_text()
                    jobs.append({'title': title, 'company': company, 'location': location, 'description': description})
                except Exception as e:
                    print(f"Failed to extract job details from {job_board['name']}: {e}")
                    continue
        browser.close()
    
    with sync_playwright() as playwright:
        run(playwright)
        
    return jobs

if __name__ == '__main__':
    with open('config/config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    
    collected_jobs = collect_job_listings(config)
    print(collected_jobs)