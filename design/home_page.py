import customtkinter
import sys
sys.path.append("D:\Desktop\Taxi Booking System")
from tkinter import *
from PIL import Image as PILImage
from tkinter import messagebox

from login_form import LoginUser

import os

from backend.customer_storage import RegisterStorage  
class Home:
    def __init__(self, home_win):
        self.home_win = home_win
        self.geometry()
        self.home_win.title("T A X I - B O O K I N G - S Y S T E M")
        self.screen_height = self.home_win.winfo_screenheight()
        self.screen_width = self.home_win.winfo_screenwidth()
        self.appearance_mode = "dark"
        self.frontend()

    def geometry(self):
        screen_width = self.home_win.winfo_screenwidth()
        screen_height = self.home_win.winfo_screenheight()
        self.home_win.geometry(f'{screen_width}x{screen_height}')
    def frontend(self):
        home_path=os.path.join(os.path.dirname(__file__), r"D:\Desktop\Taxi Booking System\assets\home.png")
        home_image = PILImage.open(home_path)
        home_widget = customtkinter.CTkImage(dark_image=home_image, light_image=home_image, size=(self.screen_width, self.screen_height))
        self.main_frame=customtkinter.CTkFrame(self.home_win,width=self.screen_width,height=self.screen_height)
        self.main_frame.place(x=0,y=0)
        main_label=customtkinter.CTkLabel(self.main_frame,text=None,image=home_widget)
        main_label.place(x=0,y=0)
        self.button=customtkinter.CTkButton(self.main_frame,text='Login',font=('helvetica',20,"bold"),fg_color="white",bg_color='white',text_color='black',hover_color='green',command=self.open_login)
        self.button.place(x=150,y=700)
        self.reg=customtkinter.CTkButton(self.main_frame,text='Register',font=('helvetica',20,"bold"),fg_color="white",bg_color='white',text_color='black',hover_color='green',command=self.choose)
        self.reg.place(x=300,y=700)
    def choose(self):
       
       self.new_popup = customtkinter.CTkToplevel(self.home_win)
       self.new_popup.title("Choose")
       self.new_popup.geometry('350x260')
       self.button = customtkinter.CTkButton(self.new_popup, width=130, height=240,text='Customer', command=self.open_registration)

       self.button.place(x=5,y=5)
       self.drivBu=customtkinter.CTkButton(self.new_popup,text='Driver',width=140,height=240,command=self.open_Driver)
       self.drivBu.place(x=145,y=5)
      
      
       window_width = self.home_win.winfo_screenwidth()
       self.new_popup.geometry(f'+{window_width - 300}+0')
       self.new_popup.resizable(False, False)
       self.new_popup.attributes('-topmost', 'true')
       self.new_popup.grab_set()  
       self.new_popup.lift()
    def open_login(self):
        self.home_win.destroy()
        login_win = customtkinter.CTk()
        login_app = LoginUser(login_win)
        login_win.after(0,lambda:login_win.state('zoomed'))
        login_win.mainloop()

    def open_registration(self):
        self.home_win.destroy()
        registration_win = customtkinter.CTk()
        from customer_registration_form import Registration
        registration_app = Registration(registration_win)
        registration_win.after(0,lambda:registration_win.state('zoomed'))
        registration_win.mainloop()
    def open_Driver(self):
        self.home_win.destroy()
        registration_win = customtkinter.CTk()
        from driver_reg import DriverRegister
        registration_app = DriverRegister(registration_win)
        registration_win.after(0,lambda:registration_win.state('zoomed'))
        registration_win.mainloop()


    

if __name__ == "__main__":
    home_win = customtkinter.CTk()
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")
    app = Home(home_win)
    home_win.after(0,lambda:home_win.state('zoomed'))
    home_win.mainloop()
