from bs4 import BeautifulSoup
import requests

class Linker:
  def __init__():
    self.url = 'https://www.linkedin.com/my-items/saved-jobs/?cardType=APPLIED'
    self.response = requests.get(self.url)
    self.soup = BeautifulSoup(self.response, 'html.parser')

    # Find the a elements with a specific class and ID
    self.div_elements = soup.find_all('a', class_='app-aware-link', id='my-id')
    l=len(self.div_elements)
    
    for i in range(self.div_elements):
      exec(f"job{i}={self.div_elements[1]}")
