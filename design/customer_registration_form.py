import customtkinter
import sys
sys.path.append("D:\\Desktop\\Taxi Booking System")
from tkinter import *
from tkinter import messagebox
from PIL import Image as PILImage
from tkinter import messagebox
from tkcalendar import DateEntry 
import os
from middleware.registration_model import CustomerRegistration
from backend.customer_storage import RegisterStorage 
from backend.customer_storage import RegisterStorage  
import re
class Registration:
    def __init__(self, driver_reg):
        self.driver_reg = driver_reg
        self.geometry()
        self.driver_reg.title("T A X I - B O O K I N G - S Y S T E M")
        self.screen_height = self.driver_reg.winfo_screenheight()
        self.screen_width = self.driver_reg.winfo_screenwidth()
        self.appearance_mode = "dark"
        self.frontend()

    def geometry(self):
        screen_width = self.driver_reg.winfo_screenwidth()
        screen_height = self.driver_reg.winfo_screenheight()
        self.driver_reg.geometry(f'{screen_width}x{screen_height}')


    def frontend(self):         
        
        reg=os.path.join(os.path.dirname(__file__), r"D:\Desktop\Taxi Booking System\assets\reg.png")
        reg_img = PILImage.open(reg)
        bge=os.path.join(os.path.dirname(__file__), r"D:\Desktop\Taxi Booking System\assets\bge.png")
        bge = PILImage.open(reg)
        self.lower_frame=customtkinter.CTkFrame(self.driver_reg,fg_color='green',width=self.screen_width,height=self.screen_height).place(x=0,y=250)
        reg_wid = customtkinter.CTkImage(dark_image=reg_img, light_image=reg_img, size=(self.screen_width, self.screen_height))
        reglab = customtkinter.CTkLabel(self.lower_frame, text=None, image=reg_wid)
        reglab.place(x=0, y=0)

        
        self.reg_frame = customtkinter.CTkFrame(self.driver_reg, width=800, height=550)
        self.reg_frame.place(x=360, y=120)
          
        self.reg_label = customtkinter.CTkLabel(self.reg_frame, text="C U S T O M E R   R  E G I S T R A T I O N", font=('bebas neue', 25, 'bold'))
        self.reg_label.place(x=150, y=20)

        self.fname_label=customtkinter.CTkLabel(self.reg_frame,text="First Name",font=('calibri', 14, 'bold'))
        self.fname_label.place(x=60,y=70)
        
        self.lname_label=customtkinter.CTkLabel(self.reg_frame,text="Last Name",font=('calibri', 14, 'bold'))
        self.lname_label.place(x=420,y=70)

        
        self.en_first_name = customtkinter.CTkEntry(self.reg_frame,width=280)
        self.en_first_name.place(x=60, y=100)
        self.en_last_name = customtkinter.CTkEntry(self.reg_frame,width=280)
        self.en_last_name.place(x=420, y=100)

        self.age=customtkinter.CTkLabel(self.reg_frame,text="Age",font=('calibri', 14, 'bold'))
        self.age.place(x=60,y=140)
        
        self.gender=customtkinter.CTkLabel(self.reg_frame,text="Gender",font=('calibri', 14, 'bold'))
        self.gender.place(x=420,y=140)
        
        self.en_age = customtkinter.CTkEntry(self.reg_frame,width=280)
        self.en_age.place(x=60, y=170)
        self.gender_var = StringVar()
        customtkinter.CTkRadioButton(self.reg_frame, text="Male", variable=self.gender_var, value=1).place(x=420, y=170)
        customtkinter.CTkRadioButton(self.reg_frame, text="Female", variable=self.gender_var, value=2).place(x=520, y=170)

        self.date_of_birth=customtkinter.CTkLabel(self.reg_frame,text="Date of Birth",font=('calibri', 14, 'bold'))
        self.date_of_birth.place(x=60,y=210)
        self.en_dob = DateEntry(self.reg_frame, selectmode='day',width=40, background='darkblue', foreground='white', borderwidth=2)
        self.en_dob.place(x=80, y=300)

        self.country=customtkinter.CTkLabel(self.reg_frame,text="Country",font=('calibri', 14, 'bold'))
        self.country.place(x=420,y=210)
       
        country_list = ['Nepal', 'Canada', 'US', 'Germany', 'UK']
        
        self.countries = StringVar()
        lists = OptionMenu(self.reg_frame, self.countries,*country_list)
        lists.config(width=36)
        self.countries.set('Select Country')
        lists.place(x=530, y=300)
        
        self.phone=customtkinter.CTkLabel(self.reg_frame,text="Phone Number",font=('calibri', 14, 'bold'))
        self.phone.place(x=60,y=270)
         
        self.email=customtkinter.CTkLabel(self.reg_frame,text="Email Address",font=('calibri', 14, 'bold'))
        self.email.place(x=420,y=270)
        self.en_phone = customtkinter.CTkEntry(self.reg_frame,width=280)
        self.en_phone.place(x=60, y=300)
        self.en_email = customtkinter.CTkEntry(self.reg_frame,width=280)
        self.en_email.place(x=420, y=300)
        self.password=customtkinter.CTkLabel(self.reg_frame,text="Password",font=('calibri', 14, 'bold'))
        self.password.place(x=60,y=340)
         
        self.re_pass=customtkinter.CTkLabel(self.reg_frame,text=" Re-Password",font=('calibri', 14, 'bold'))
        self.re_pass.place(x=420,y=340)
        self.en_pass = customtkinter.CTkEntry(self.reg_frame, show="*",width=280)
        self.en_pass.place(x=60, y=370)

        self.en_re_pass = customtkinter.CTkEntry(self.reg_frame, show="*",width=280)
        self.en_re_pass.place(x=420, y=370)
        self.register_button = customtkinter.CTkButton(self.reg_frame, text="Register", width=280, command=self.register)
        self.register_button.place(x=60, y=430)
        self.signin = customtkinter.CTkButton(self.reg_frame, text="Already have an account! Login?", width=280,command=self.open_login)
        self.signin.place(x=420, y=430)
    def register(self):
        first_name = self.en_first_name.get()
        last_name = self.en_last_name.get()
        age = self.en_age.get()
        gender = "Male" if self.gender_var.get() == 1 else "Female"
        dob = self.en_dob.get_date()
        country = self.countries.get()
        phone=self.en_phone.get()
        email = self.en_email.get()
        password = self.en_pass.get()
        id=0
        re_enter_password = self.en_re_pass.get()
        if not (first_name and last_name and age and gender and dob and country and phone and email and password and re_enter_password):
            messagebox.showerror("Error", "Please fill in all fields.")
            return
        try:
            age = int(age)
            if age <= 0:
                raise ValueError("Invalid age")
        except ValueError:
            messagebox.showerror("Error", "Age must be a positive integer.")
            return
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("Error", "Invalid email address.")
            return
        try:
            phone = int(phone)
            if phone <= 0:
                raise ValueError("Invalid phone number")
        except ValueError:
            messagebox.showerror("Error", "Phone number must be a positive integer.")
            return

    
        if first_name!='' and last_name!='' and age!='' and gender!='' and phone!='' and dob!='' and country!='' and email!='' and password!='':
            cus=CustomerRegistration(id,first_name , last_name ,age ,gender , dob,country,phone, email, password )
            reg_storage = RegisterStorage()
            success = reg_storage._CustomerRegistration(cus)

            if success:
                message = f"Registred Successfully as  {first_name} {last_name}"
                messagebox.showinfo("Success", message)
            else:
                messagebox.showerror("Error", "Registration failed.")

            if password != re_enter_password:
                messagebox.showerror("Error", "Passwords do not match.")
                return
    def open_login(self):
        self.driver_reg.destroy()
        
        from login_form import LoginUser
        login_win = customtkinter.CTk()
        login_app = LoginUser(login_win)
        login_win.after(0,lambda:login_win.state('zoomed'))
        login_win.mainloop()


if __name__ == "__main__":
    driver_reg = customtkinter.CTk()
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")
    app = Registration(driver_reg)
    driver_reg.after(0, lambda: driver_reg.state('zoomed'))
    driver_reg.mainloop()
