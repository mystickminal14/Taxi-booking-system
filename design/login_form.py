import customtkinter
import sys
sys.path.append("D:\Desktop\Taxi Booking System")
from tkinter import *
from tkinter import messagebox
from PIL import Image as PILImage
from middleware.login_model import CustomerLogin

from backend.customer_storage import RegisterStorage 
import os
from backend.storage import Storage

from backend.customer_storage import RegisterStorage  
class LoginUser:
    def __init__(self, log_win):
        self.log_win = log_win
        self.geometry()
        self.log_win.title("T A X I - B O O K I N G - S Y S T E M")
        self.screen_height = self.log_win.winfo_screenheight()
        self.connection = Storage.Connect()
        self.appearance_mode = "dark"

        self.frontend()
    def geometry(self):
        screen_width = self.log_win.winfo_screenwidth()
        screen_height = self.log_win.winfo_screenheight()
        print(screen_height)
        print(screen_width)
        self.log_win.geometry(f'{screen_width}x{screen_height}')
    def frontend(self):         
        self.left_panel(self.log_win)    
        right_frame = customtkinter.CTkFrame(self.log_win, width=500, height=self.screen_height)
        right_frame.place(x=1080, y=0)
        logo_path=os.path.join(os.path.dirname(__file__), r"D:\Desktop\Taxi Booking System\assets\logo.png")
        logo_image = PILImage.open(logo_path)
        logo_widget = customtkinter.CTkImage(dark_image=logo_image, light_image=logo_image, size=(55, 50))
      
        logo_label = customtkinter.CTkLabel(right_frame, text=None, image=logo_widget)
        logo_label.place(x=5, y=20)
        switch_one = customtkinter.StringVar(value='on')
        
        def toggle_mode():
            if switch_one.get() == 'on':
                customtkinter.set_appearance_mode("dark")
            
            else:
                customtkinter.set_appearance_mode("light")
               
        
        toggle = customtkinter.CTkSwitch(right_frame, text=None, command=toggle_mode, variable=switch_one, onvalue='on', offvalue='off')
        toggle.place(x=400, y=50)

        login_label=customtkinter.CTkLabel(right_frame,text='L O G I N',font=('helvetica',30,'bold'))
        login_label.place(x=35,y=200)

        username=customtkinter.CTkLabel(right_frame,text='USERNAME ',font=('courier new',16,'bold'))
        username.place(x=35,y=250)
        self.user_entry=customtkinter.CTkEntry(right_frame,placeholder_text="enter your user-name",width=390,height=45)
        self.user_entry.place(x=35,y=280)
        passcode=customtkinter.CTkLabel(right_frame,text='PASSWORD ',font=('courier new',16,'bold'))
        passcode.place(x=35,y=335)
        self.passcode_entry=customtkinter.CTkEntry(right_frame,placeholder_text="enter your password", show="*",width=390,height=45)
        self.passcode_entry.place(x=35,y=365)

        self.login_btn=customtkinter.CTkButton(right_frame,text='Login',font=('arial',16), width=390,height=36,command=self.login)

        self.login_btn.place(x=35,y=430)
        
        or_lab=customtkinter.CTkLabel(right_frame,text='OR ',font=('courier new',16,'bold'))
        or_lab.place(x=220,y=470)
        
        register_btn=customtkinter.CTkButton(right_frame,text='Sign-up',font=('arial',16), width=390,height=36,command=self.choose)
        register_btn.place(x=35,y=500)
    
    def left_panel(self,left):
        image_path = os.path.join(os.path.dirname(__file__), r"D:\Desktop\Taxi Booking System\assets\login.png")      
        original_img = PILImage.open(image_path)
        alpha = 140 
        transparent_img = original_img.copy()
        transparent_img.putalpha(alpha)   
        self.left_frame=customtkinter.CTkFrame(left,width=1100,height=self.screen_height)
        self.left_frame.place(x=0,y=0)
        log_img = customtkinter.CTkImage(dark_image=transparent_img,light_image=transparent_img, size=(1100, self.screen_height))   
        image_label = customtkinter.CTkLabel(self.left_frame, text=None, image=log_img)
        image_label.place(x=0, y=0)
    def log_out(self):
        self.log_win.destroy()
        dash_win = customtkinter.CTk()
        from customer_registration_form import Registration
        dash_app = Registration(dash_win)
        dash_win.after(0,lambda:dash_win.state('zoomed'))
        dash_win.mainloop()
    def login(self):
        useremail = self.user_entry.get()
        pass_code = self.passcode_entry.get()
        login = CustomerLogin(_username=useremail, _password=pass_code)
        conec_reg = RegisterStorage()
        cus = conec_reg.CustomerLogin(login)
        cus2= conec_reg.ManagerLogin(login)
        cus3=conec_reg.DriverLogin(login)
   
        
        if not useremail or not pass_code:
            messagebox.showerror("Login Failed", "Please enter both username and password.")
            return
        if cus != None :

            import gobal
            gobal.customer = cus
            messagebox.showinfo("Login Success", "Welcome Customer!")
            self.log_win.destroy()
            dash_win = customtkinter.CTk()
            from customer_dashboard import Dashboard
            dash_app = Dashboard(dash_win)
            dash_win.after(0,lambda:dash_win.state('zoomed'))
            dash_win.mainloop()
        elif cus2!=None:
          
                import gobal
                gobal.manager=cus2
                print(cus2)
                print(gobal.customer)
                messagebox.showinfo("Login Success", "Welcome Admin!")
                self.log_win.destroy()
                dump = customtkinter.CTk()
                from manager_dashboard import Dashboard
                dash_app = Dashboard(dump)
                dump.after(0,lambda:dump.state('zoomed'))
                dump.mainloop()
        elif cus3!=None:
             import gobal
             gobal.driver=cus3
             messagebox.showinfo("Login Success", "Welcome Driver!")
             self.log_win.destroy()
             dump = customtkinter.CTk()
             from driver_dash import Dashboard
             dash_app = Dashboard(dump)
             dump.after(0,lambda:dump.state('zoomed'))
             dump.mainloop()

        
        else : 
               messagebox.WARNING("Login Error", "Invalid!")
         
     
    def choose(self):
       self.new_popup = customtkinter.CTkToplevel(self.log_win)
       self.new_popup.title("Choose")
       self.new_popup.geometry('350x260')
       self.button = customtkinter.CTkButton(self.new_popup, width=130, height=240,text='Customer', command=self.open_registration)
       self.button.place(x=5,y=5)
       self.drivBu=customtkinter.CTkButton(self.new_popup,text='Driver',width=140,height=240,command=self.open_Driver)
       self.drivBu.place(x=145,y=5)
       window_width = self.log_win.winfo_screenwidth()
       self.new_popup.geometry(f'+{window_width - 300}+0')
       self.new_popup.resizable(False, False)
       self.new_popup.attributes('-topmost', 'true')
       self.new_popup.grab_set()  
       self.new_popup.lift()
    def open_registration(self):
        self.log_win.destroy()
        registration_win = customtkinter.CTk()
        from customer_registration_form import Registration
        registration_app = Registration(registration_win)
        registration_win.after(0,lambda:registration_win.state('zoomed'))
        registration_win.mainloop()
    def open_Driver(self):
        self.log_win.destroy()
        registration_win = customtkinter.CTk()
        from driver_reg import DriverRegister
        registration_app = DriverRegister(registration_win)
        registration_win.after(0,lambda:registration_win.state('zoomed'))
        registration_win.mainloop()

if __name__ == "__main__":
    log_win = customtkinter.CTk()
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")
    app = LoginUser(log_win)
    log_win.after(0,lambda:log_win.state('zoomed'))
    log_win.mainloop()
