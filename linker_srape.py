from bs4 import BeautifulSoup
import requests

class LinkerScrape:
  def __init__():
    
    #define fixed values
    self.url = 'https://www.linkedin.com/my-items/saved-jobs/?cardType=APPLIED'
    self.response = requests.get(self.url)
    self.soup = BeautifulSoup(self.response, 'html.parser')
  def get_jobs():
    self.jobs=[]
    # Send a POST request with the login data and check if it was successful
    if requests.post(self.login_url, json={'username': self.username, 'password': self.password}).ok:
        login=True
    else:
        login=False
  
    # Find the a elements with a specific class and ID
    self.div_elements = soup.find_all('a', class_='app-aware-link', id='my-id')
    l=len(self.div_elements)
    
    for jobnames in self.div_elements:
      exec(f"{jobnames}={self.div_elements[jobnames]}")
    
    for jobs in self.div_elements:
      self.jobs.append(jobs)
