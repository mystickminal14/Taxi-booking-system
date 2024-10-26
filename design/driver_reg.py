import customtkinter
from tkinter import *
from customer_registration_form import Registration  
from tkinter import messagebox
from middleware.driv_model import DriverRegistration
from backend.customer_storage import RegisterStorage 
import re
class DriverRegister(Registration):
    def __init__(self, driver_reg):
        super().__init__(driver_reg) 

    def frontend(self):
        super().frontend()
        self.reg_label=customtkinter.CTkLabel(self.reg_frame,text="D R I V E R  R E G I S T R A T I O N", font=('bebas neue', 25, 'bold'))
        self.reg_label.place(x=150, y=20)
       
        self.driver_label = customtkinter.CTkLabel(self.reg_frame, text="Driver License Number", font=('calibri', 14, 'bold'))
        self.driver_label.place(x=60, y=410)

        self.exp_label = customtkinter.CTkLabel(self.reg_frame, text="Total years of experience", font=('calibri', 14, 'bold'))
        self.exp_label.place(x=420, y=410)

        self.en_dlcn = customtkinter.CTkEntry(self.reg_frame, width=280)
        self.en_dlcn.place(x=60, y=440)

        self.en_exp = customtkinter.CTkEntry(self.reg_frame, width=280)
        self.en_exp.place(x=420, y=440)

        self.register_button.place(x=60, y=490)
        self.signin.place(x=420, y=490)
    def register(self):
    
        id=0
        first_name = self.en_first_name.get()
        last_name = self.en_last_name.get()
        age = self.en_age.get()
        gender = "Male" if self.gender_var.get() == 1 else "Female"
        dob = self.en_dob.get_date()
        country = self.countries.get()
        phone = self.en_phone.get()
        email = self.en_email.get()
        password = self.en_pass.get()
        dlcn = self.en_dlcn.get()
        exp = self.en_exp.get()

        if password != self.en_re_pass.get():
            messagebox.showerror("Error", "Passwords do not match.")
            return
        try:
            pass
        except Exception as e:
          raise Exception(f"Error connecting to the database: {e}")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("Error", "Invalid email address.")
            return
        try:
            exp = int(exp)
            if exp <= 0:
                raise ValueError("Invalid years of experience")
        except ValueError:
            messagebox.showerror("Error", "Total years of experience must be a positive integer.")
            return

        drivers = DriverRegistration(id,first_name, last_name, age, gender, dob, country, phone, email, password, dlcn, exp)
        reg_storage = RegisterStorage()
        success = reg_storage._DriverRegistration(drivers)

        if success:
            message = f"Registered Successfully as {first_name} {last_name}"
            messagebox.showinfo("Success", message)
        else:
            messagebox.showerror("Error", "Registration failed.")
    
    
if __name__ == "__main__":
    driver_reg = customtkinter.CTk()
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")
    app = DriverRegister(driver_reg)
    driver_reg.after(0, lambda: driver_reg.state('zoomed'))
    driver_reg.mainloop()
