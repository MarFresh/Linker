from customtkinter import *
from tkinter import *

class LinkerUi:
  def __init__(self):
    pass
  def cookies(selection):
    cookie=appearance_mode_optionemenu.get()
  def login(self):
    login=CTk()
    title=Label(login, text="LinkedIn Credentials").pack()
    e=CTkEntry(login, placeholder="Linked Email").pack()
    p=CTkEntry(login, placeholder="Linked Password").pack()
    submit=CTkButton(login, text="Login", command=send).pack()
    login.mainloop()
  def send(self):
    self.password=p.get()
    self.email=e.get()
    login.destroy()
  def get_password(self):
    return self.password
  def get_email(self):
    return self.email
  def main(self):
    main=CTk()
    self.title("CustomTkinter complex_example.py")
    geometry(f"{1100}x{580}")
    
    # configure grid layout (4x4)
    grid_columnconfigure(1, weight=1)
    grid_columnconfigure((2, 3), weight=0)
    grid_rowconfigure((0, 1, 2), weight=1)

    # create sidebar frame with widgets
    sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
    sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
    sidebar_frame.grid_rowconfigure(4, weight=1)
    logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="CustomTkinter", font=customtkinter.CTkFont(size=20, weight="bold"))
    logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
    sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Applied Jobs", command=self.ajobs)
    sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
    appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
    appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
    appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                   command=self.change_appearance_mode_event)
    appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
    scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
    scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
    scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                           command=self.change_scaling_event)
    scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))
    
    self.appearance_mode_optionemenu.set("Dark")
    cookie=
    self.scaling_optionemenu.set("100%")
  def ajobs(self):
    main.destroy()
    main=CTk()
    self.title("Jobs")
    geometry(f"{1100}x{580}")
    
    # configure grid layout (4x4)
    grid_columnconfigure(1, weight=1)
    grid_columnconfigure((2, 3), weight=0)
    grid_rowconfigure((0, 1, 2), weight=1)

    # create sidebar frame with widgets
    sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
    sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
    sidebar_frame.grid_rowconfigure(4, weight=1)
    logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="CustomTkinter", font=customtkinter.CTkFont(size=20, weight="bold"))
    logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
    sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Applied Jobs", command=self.ajobs)
    sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
    appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
    appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
    appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                   command=self.change_appearance_mode_event)
    appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
    scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
    scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
    scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                           command=self.change_scaling_event)
    scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

    self.jobwi = customtkinter.CTkFrame(self)
    
    appearance_mode_optionemenu.set(cookie)
    scaling_optionemenu.set("100%")

    self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("CTkTabview")
        self.tabview.add("Tab 2")
        self.tabview.add("Tab 3")
        self.tabview.tab("CTkTabview").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Tab 2").grid_columnconfigure(0, weight=1)
    
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
