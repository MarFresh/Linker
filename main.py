from bs4 import BeautifulSoup
import requests
from customtkinter import *
class Linker:
  def __init__():
    #set apearance
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")
    #define fixed values
    self.url = 'https://www.linkedin.com/my-items/saved-jobs/?cardType=APPLIED'
    self.response = requests.get(self.url)
    self.soup = BeautifulSoup(self.response, 'html.parser')
    
    start(self):
      app = CTk()
      app.geometry("400x780")
      app.title("CustomTkinter simple_example.py")
      title=CTkLabel(text="LinkedIn Credentials")
      e=CTkEntry(placeholder="LinkedIn Email").pack()
      p=CTkEntry(placeholder="LinkedIn Password").pack()
      app.mainloop()
      # Send a POST request with the login data and check if it was successful
      if requests.post(self.login_url, json={'username': self.username, 'password': self.password}).ok:
          login=True
      else:
          login=False
  
      # Find the a elements with a specific class and ID
      self.div_elements = soup.find_all('a', class_='app-aware-link', id='my-id')
      l=len(self.div_elements)
      
      for i in range(self.div_elements):
        exec(f"job{i}={self.div_elements[i]}")
