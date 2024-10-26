import os
import sys
import tkinter as tk
sys.path.append("D:/Desktop/Taxi Booking System")
from tkinter import messagebox
from backend.storage import Storage
from PIL import Image as PILImage
import datetime as dt
from tkinter import *
from time import strftime
from tkcalendar import DateEntry  
import customtkinter
import tkintermapview
from middleware.reserve import BookRide
from backend.customer_storage import RegisterStorage
import gobal

from tkinter import ttk

class Dashboard:
    def __init__(self, driver_root):
        self.driver_root = driver_root
        self.driver_root.title("T A X I - B O O K I N G - S Y S T E M")
        self.appearance_mode = "dark"
        self.screen_width = self.driver_root.winfo_screenwidth()
        self.screen_height = self.driver_root.winfo_screenheight()
        self.geometry()
        self.connection = Storage.Connect()
        self.managerFrontend()
   
    def geometry(self):
        screen_width = self.driver_root.winfo_screenwidth()
        screen_height = self.driver_root.winfo_screenheight()
        self.driver_root.geometry(f'{screen_width}x{screen_height}')
    
    def user_profile(self):
       
       self.new_popup = customtkinter.CTkToplevel(self.driver_root)
       self.new_popup.title("M A N A G E R -  P R O F I L E")
       self.new_popup.geometry('350x350')

       self.fullName = customtkinter.CTkLabel(self.new_popup, text="Full Name:", font=('calibri', 18, 'bold'), width=120)
       self.fullName.place(x=10, y=10)

       full_name_text = f"{gobal.driver[1]} {gobal.driver[2]}"
       self.fullNameEn = customtkinter.CTkLabel(self.new_popup, text=full_name_text, font=('calibri', 18, 'bold'))
       self.fullNameEn.place(x=140, y=10)

       self.age = customtkinter.CTkLabel(self.new_popup, text="Age:", font=('calibri', 18, 'bold'), width=120)
       self.age.place(x=10, y=40)
    
       self.ageen = customtkinter.CTkLabel(self.new_popup, text=gobal.driver[4], font=('calibri', 18, 'bold'))
       self.ageen.place(x=140, y=40)
    
       self.ADDRESS = customtkinter.CTkLabel(self.new_popup, text="Phone:", font=('calibri', 18, 'bold'), width=120)
       self.ADDRESS.place(x=10, y=130)
    
       self.add = customtkinter.CTkLabel(self.new_popup, text=gobal.driver[6], font=('calibri', 18, 'bold'))
       self.add.place(x=140, y=130)

       self.pn = customtkinter.CTkLabel(self.new_popup, text="Country:", font=('calibri', 18, 'bold'), width=120)
       self.pn.place(x=10, y=160)
    
       self.pen = customtkinter.CTkLabel(self.new_popup, text=gobal.driver[5], font=('calibri', 18, 'bold'))
       self.pen.place(x=140, y=160)
       self.email = customtkinter.CTkLabel(self.new_popup, text="Email:", font=('calibri', 18, 'bold'), width=120)
       self.email.place(x=10, y=190)
    
       self.em = customtkinter.CTkLabel(self.new_popup, text=gobal.driver[2], font=('calibri', 18, 'bold'))
       self.em.place(x=140, y=190)
       self.passcode = customtkinter.CTkLabel(self.new_popup, text="Password:", font=('calibri', 18, 'bold'), width=120)
       self.passcode.place(x=10, y=220)
       self.license = customtkinter.CTkLabel(self.new_popup, text=gobal.driver[10], font=('calibri', 18, 'bold'))
       self.license.place(x=140, y=250)
       self.lic = customtkinter.CTkLabel(self.new_popup, text="Password:", font=('calibri', 18, 'bold'), width=120)
       self.lic.place(x=10, y=280)
    
       self.pw = customtkinter.CTkLabel(self.new_popup, text=gobal.driver[11], font=('calibri', 18, 'bold'))
       self.pw.place(x=140, y=310)
       window_width = self.driver_root.winfo_screenwidth()
       self.new_popup.geometry(f'+{window_width - 300}+0')
       self.new_popup.resizable(False, False)
       self.new_popup.attributes('-topmost', 'true')
       self.new_popup.lift()
    def managerFrontend(self):
       upper_panel=customtkinter.CTkFrame(self.driver_root,width=230,height=100,fg_color="skyblue").place(x=0,y=0)
       self.UpperPanel(upper_panel)
       left_panel=customtkinter.CTkFrame(self.driver_root,width=230,height=self.screen_height)
       left_panel.place(x=0,y=110)
       self.left(left_panel)
       self.logout=customtkinter.CTkButton(left_panel,text='Logout',command=self.log_out)
       self.logout.place(x=10,y=570)
        
       title_panel = customtkinter.CTkFrame(self.driver_root, width=self.screen_width, height=100, fg_color="#05695A").place(x=240, y=0)
       self.TitlePanel(title_panel)
       user = os.path.join(os.path.dirname(__file__), r"D:\Desktop\Taxi Booking System\assets\users.png")
       user_im = PILImage.open(user)
       user_wid = customtkinter.CTkImage(dark_image=user_im, light_image=user_im, size=(120, 120))

       riders = os.path.join(os.path.dirname(__file__), r"D:\Desktop\Taxi Booking System\assets\booked.png")
       user_ride = PILImage.open(riders)
       user_ride_wid = customtkinter.CTkImage(dark_image=user_ride, light_image=user_ride, size=(140, 110))

       driver = os.path.join(os.path.dirname(__file__), r"D:\Desktop\Taxi Booking System\assets\driver.png")
       drover = PILImage.open(driver)
       user_drover= customtkinter.CTkImage(dark_image=drover, light_image=drover, size=(130, 110))
       
       
       inactive = os.path.join(os.path.dirname(__file__), r"D:\Desktop\Taxi Booking System\assets\rund.png")
       inactive_img = PILImage.open(inactive)
       inactive_wid= customtkinter.CTkImage(dark_image=inactive_img, light_image=inactive_img, size=(150, 120))
       first_box=customtkinter.CTkFrame(self.driver_root,width=430,height=160)
       first_box.place(x=240,y=110)
       self.first=customtkinter.CTkButton(first_box,width=430,text=" Booking",height=160,fg_color='#04473D',image=user_wid, compound=tk.TOP,text_color='black',font=("league spartan", 20, 'bold') ,command=lambda: self.switch_tab("BOOKING"))
       self.first.place(x=0,y=0)
       second_box=customtkinter.CTkFrame(self.driver_root,width=430,height=160)
       second_box.place(x=680,y=110)
       self.second=customtkinter.CTkButton(second_box,text=" History",width=430,height=160,image=user_ride_wid, compound=tk.TOP,fg_color='#04473D',text_color='black',font=("league spartan", 20, 'bold'), command=lambda: self.switch_tab("HISTORY"))
       self.second.place(x=0,y=0)
       third_box=customtkinter.CTkFrame(self.driver_root,width=430,height=160)
       third_box.place(x=1120,y=110)
       self.third=customtkinter.CTkButton(third_box,text="Rating",width=400,height=160,image=user_drover, compound=tk.TOP,fg_color="#04473D",text_color='black',font=("league spartan", 20, 'bold'), command=lambda: self.switch_tab("CUSTOMER RATING"))
       self.third.place(x=0,y=0)
  

       tabs=customtkinter.CTkTabview(self.driver_root,width=1265,height=500,fg_color="#A9C487",anchor='nw',text_color='white',segmented_button_fg_color="black",segmented_button_unselected_hover_color='skyblue',segmented_button_unselected_color='black',segmented_button_selected_color='#A9C487',segmented_button_selected_hover_color="skyblue")
       tabs.place(x=240,y=280)

       self.tabs = tabs 
       tabs.add("BOOKING")
       self.book(tabs.tab("BOOKING"))
       tabs.add("HISTORY")
       self.history(tabs.tab("HISTORY"))

       tabs.add("CUSTOMER RATING")
    
    def log_out(self):
        self.driver_root.destroy()
        dash_win = customtkinter.CTk()
        from login_form import LoginUser
        dash_app = LoginUser(dash_win)
        dash_win.after(0,lambda:dash_win.state('zoomed'))
        dash_win.mainloop()
    def history(self,up):
        self.search=customtkinter.CTkEntry(up,font=("league spartan", 12, 'bold'),placeholder_text="Search",width=200)
        self.search.place(x=10,y=3)
        self.se=customtkinter.CTkButton(up,text="Search",width=80,font=("league spartan", 12, 'bold'))
        self.se.place(x=220,y=3)
      
        self.regis=customtkinter.CTkButton(up,text="Delete",font=("league spartan", 12, 'bold'))
        self.regis.place(x=1094,y=3)
        
        column = ("Booking_id","Location", "Destination","time","date","status")
        self.ac_booking = ttk.Treeview(up, columns=column, show="headings", height=24)

        for col in column:
            self.ac_booking.heading(col, text=col, anchor="center")
            self.ac_booking.column(col, anchor="center",width=300)
       
        
        self.view_bookings()
        self.ac_booking.place(x=5,y=50)
    def view_bookings(self):
        ID=gobal.driver[0]
        try:
            with self.connection.cursor() as cursor:
                 query = "SELECT `book_id`, `location`, `destination`, `time`, `date`, `status` FROM `reservation` WHERE `driver_id` = %s"
                 cursor.execute(query, (ID,))
                 rows = cursor.fetchall()

            for item in self.ac_booking.get_children():
                self.ac_booking.delete(item)

            for row in rows:
                self.ac_booking.insert(parent='', index='end', values=(row[0], row[1], row[2], row[3], row[4],row[5]))

        except Exception as err:
            print(f"Error: {err}")

    def left(self,bloom):
        full_name=customtkinter.CTkLabel( bloom, text="FULL NAME ", font=('calibri', 18, 'bold'))
        full_name.place(x=10,y=20)
        fn=customtkinter.CTkLabel( bloom, text=f'{gobal.driver[1]},{gobal.driver[2]}', font=('calibri', 18, 'bold'))
        fn.place(x=10,y=50)

        age=customtkinter.CTkLabel( bloom, text="AGE ", font=('calibri', 18, 'bold'))
        age.place(x=10,y=90)
        an=customtkinter.CTkLabel( bloom, text=gobal.driver[3], font=('calibri', 18, 'bold'))
        an.place(x=10,y=120)

        pn=customtkinter.CTkLabel( bloom, text="PHONE ", font=('calibri', 18, 'bold'))
        pn.place(x=10,y=160)
        phone=customtkinter.CTkLabel( bloom, text=gobal.driver[6], font=('calibri', 18, 'bold'))
        phone.place(x=10,y=190)

        add=customtkinter.CTkLabel( bloom, text="GENDER ", font=('calibri', 18, 'bold'))
        add.place(x=10,y=230)
        fadren=customtkinter.CTkLabel( bloom, text=gobal.driver[4], font=('calibri', 18, 'bold'))
        fadren.place(x=10,y=260)
        email=customtkinter.CTkLabel( bloom, text="DATE OF BIRTH", font=('calibri', 18, 'bold'))
        email.place(x=10,y=300)
        em=customtkinter.CTkLabel( bloom, text=gobal.driver[5], font=('calibri', 18, 'bold'))
        em.place(x=10,y=330)

        COUNTRY=customtkinter.CTkLabel( bloom, text="COUNTRY ", font=('calibri', 18, 'bold'))
        COUNTRY.place(x=10,y=370)
        coun=customtkinter.CTkLabel( bloom, text=gobal.driver[7], font=('calibri', 18, 'bold'))
        coun.place(x=10,y=400)
        username=customtkinter.CTkLabel( bloom, text="DATE OF BIRTH", font=('calibri', 18, 'bold'))
        username.place(x=10,y=440)
        userem=customtkinter.CTkLabel( bloom, text=gobal.driver[5], font=('calibri', 18, 'bold'))
        userem.place(x=10,y=470)


    def switch_tab(self, tab_name):
        self.tabs.set(tab_name) 
    def TitlePanel(self,title):  
        wel_label = customtkinter.CTkLabel(title, text="Welcome! Mr. Minal to your dashboard!", font=("league spartan", 40, 'bold'), text_color='black', bg_color='#05695A')
        wel_label.place(x=300, y=24)  
        
        bell_path = os.path.join(os.path.dirname(__file__), r"D:\Desktop\Taxi Booking System\assets\bell.png")
        mail_path = os.path.join(os.path.dirname(__file__), r"D:\Desktop\Taxi Booking System\assets\mail.png")
        nepal_path = os.path.join(os.path.dirname(__file__), r"D:\Desktop\Taxi Booking System\assets\nepal.png")
       
        bell_image = PILImage.open(bell_path)
        mail_image = PILImage.open(mail_path)
        nepal_image = PILImage.open(nepal_path)

        bell_widget = customtkinter.CTkImage(dark_image=bell_image, light_image=bell_image, size=(33, 33))
        bell_label = customtkinter.CTkLabel(title, text=None, image=bell_widget,bg_color='#05695A')
        bell_label.place(x=1250, y=2)

        mail_widget = customtkinter.CTkImage(dark_image=mail_image, light_image=mail_image, size=(50, 35))
        mail_label = customtkinter.CTkLabel(title, text=None, image=mail_widget,bg_color='#05695A')
        mail_label.place(x=1280, y=2)

        nepal_widget = customtkinter.CTkImage(dark_image=nepal_image, light_image=nepal_image, size=(50, 33))
        nepal_label = customtkinter.CTkLabel(title, text=None,  image=nepal_widget,bg_color='#05695A')
        nepal_label.place(x=1320, y=2)
        
        switch_one = customtkinter.StringVar(value='on')
        def toggle_mode():
            if switch_one.get() == 'on':
                customtkinter.set_appearance_mode("dark")
            else:
                customtkinter.set_appearance_mode("light")
              
        toggle = customtkinter.CTkSwitch(title, text=None, command=toggle_mode, variable=switch_one, onvalue='on',bg_color="#05695A", offvalue='off')
        toggle.place(x=1360, y=2)

        name_label=customtkinter.CTkButton(title,text="PROFILE",font=('calibri',16,'bold'),width=120,command=self.user_profile)
        name_label.place(x=1410,y=2)
      
    def UpperPanel(self,up):
           taxi_label=customtkinter.CTkLabel(up,text="T A X I ",font=("league spartan",30,'bold'),text_color='black',bg_color='skyblue').place(x=55,y=2)
           sys_label=customtkinter.CTkLabel(up,text="S Y S T E M",font=("league spartan",30,'bold'),text_color='black',bg_color='skyblue').place(x=26,y=44)
           

    def book(self,book_table):
        paisa=customtkinter.CTkLabel(book_table,text="Total Charge :",text_color="black" ,font=("league spartan",15,'bold'))
        paisa.place(x=20,y=3)
        self.paisa_en=customtkinter.CTkEntry(book_table,width=220)
        self.paisa_en.place(x=140,y=4)
        accept=customtkinter.CTkButton(book_table,text='Accept',command=self.updateClick)
        accept.place(x=1094,y=5)
        column = ("Booking Id","Customer ID","Customer Name","Location", "Destination","Time","Date","Status")
        self.tree_booking = ttk.Treeview(book_table, columns=column, show="headings", height=24)
        for col in column:
            self.tree_booking.heading(col, text=col, anchor="center")
            self.tree_booking.column(col, anchor="center",width=190)
       
 
        self.book_record()
        self.tree_booking.place(x=10,y=50)
    def updateClick(self):
        selected_item = self.tree_booking.selection()
        if selected_item:
           book_id = self.tree_booking.item(selected_item)['values'][0]
           
           self.updateStatus(book_id, 'accepted')
           self.Inser()

           messagebox.showinfo("Success", "Ride accepted Successfully")
           self.view_bookings()
           
        else:
            messagebox.showerror("Invalid ", "Please select a row to make inactive")
   
  

    def Inser(self):
        id=gobal.driver[0]
        paisa=self.paisa_en.get()
        try:
            with self.connection.cursor() as cursor:
               query = f"INSERT INTO `payment`( `price`, `driver_id`)"
               self.bookings()
               cursor.execute(query, (paisa, id))
               self.connection.commit()
               
        except Exception as err:
    
            print(f"Error updating status: {err}")
    def updateStatus(self, book_id, new_status):
        try:
            with self.connection.cursor() as cursor:
               query = f"UPDATE `reservation` SET `status` = %s WHERE `book_id` = %s"

               cursor.execute(query, (new_status, book_id))
               self.connection.commit()
               self.bookings()
               self.view_bookings()
        except Exception as err:
            print(f"Error updating status: {err}")
    def book_record(self):
        try:
            with self.connection.cursor() as cursor:
                query = f"""SELECT 
    reservation.book_id,
    reservation.customer_id,
    CONCAT(customer_registration.firstName, ' ', customer_registration.lastName) AS customer_full_name,
    reservation.location,
    reservation.destination,
    reservation.time,
    reservation.date,
   
    reservation.status
FROM 
    reservation
JOIN 
    customer_registration ON reservation.customer_id = customer_registration.customer_id;

"""
                cursor.execute(query)
                rows = cursor.fetchall()

                for item in self.tree_booking.get_children():
                    self.tree_booking.delete(item)
                for row in rows:
                    self.tree_booking.insert(parent='', index='end', values=(row[0], row[1], row[2], row[3], row[4],row[5],row[6],row[7]))
        except Exception as err:
            print(f"Error: {err}")
  


if __name__ == "__main__":
    driver_root = customtkinter.CTk()
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue") 
    driver_root.after(0,lambda:driver_root.state('zoomed'))
    user_dash = Dashboard(driver_root)
    driver_root.mainloop()
 

     
        
       

   
       



