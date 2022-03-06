from bs4 import BeautifulSoup
import requests
import time

def find_job(unfamiliar_skill):
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index , job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ','')
            skills = job.find('span', class_='srp-skills').text.replace(' ','')      
            more_info = job.header.h2.a['href']
            # Converting the String to list by spliting on the bases of ","
            skills_list = str(skills.strip().upper()).split(",")
            # Initalising a FLAG with False 
            # This will be used to keep track if the unfamiler skills are found or no 

            UNFAMILIAR_SKILL_FLAG = False
            # Looping into Each element of inputed UNSKILLES SKILLS
            # value variable contains a single elemnt for eg. JAVA
            for value in unfamiliar_skill:
                # Its compared if its in the skill_list then we dont need this data ..
                # So The UNFAMILIAR_SKILL_FLAG is set to true Indicating that we have found a  Unfamiler skill
     
                if value.upper() in skills_list:
                    UNFAMILIAR_SKILL_FLAG = True
            # Here It's checked if the current data has UNFAMILIAR_SKILL 
            # if False then ..Add the current data to jobs.txt
            if UNFAMILIAR_SKILL_FLAG == False:
                with open(f'jobs.txt','a') as f:
                    f.write(f"Company name: {company_name.strip()} \n")
                    f.write(f"Required skills: {skills.strip()}\n")
                    f.write(f"More Info: {more_info} \n\n")
                    f.write(f"-------------------\n")
                
            # if unfamiliar_skills not in skills.upper():
if __name__ == '__main__':
    while True:
        print('skills you are unfamilar with (Seprated with ","):')
        unfamiliar_skills = input('-->').upper()
        # String to list with "," as sepreator 
        unfamiliar_skills_list = unfamiliar_skills.split(",")

        print(f'filtering out {unfamiliar_skills} skills...')
        find_job(unfamiliar_skills_list)
        print("Done ")
        
