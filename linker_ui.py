from customtkinter import *
from tkinter import *

class LinkerUi:
  def __init__(self):
    pass
  def login(self):
    login=CTk()
    title=Label(login, text="LinkedIn Credentials").pack()
    e=CTkEntry(login, placeholder="Linked Email").pack()
    p=CTkEntry(login, placeholder="Linked Password").pack()
    submit=CTkButton(login, text="Login", command=send).pack()
    login.mainloop()
  def send(self):
    pass
  def get_password(self):
    return self.password
  def get_email(self):
    return self.email
