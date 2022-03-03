from bs4 import BeautifulSoup
import requests
import time

print('skills you are unfamilar with(in CAPS):')
unfamiliar_skills = input('-->')
print(f'filtering out {unfamiliar_skills} skills...')

def find_job():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for job in jobs:
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ','')
            skills = job.find('span', class_='srp-skills').text.replace(' ','')      
            more_info = job.header.h2.a['href']
            if unfamiliar_skills not in skills.upper():
                print(f"Company name: {company_name.strip()}")
                print(f"Required skills: {skills.strip()}")
                print(f"More Info: {more_info}")
                print('') 

if __name__ == '__main__':
    while True:
        find_job()
        time_wait = 10
        time.sleep(time_wait * 60)
