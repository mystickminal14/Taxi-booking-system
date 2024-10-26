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
    def __init__(self, manager_root):
        self.manager_root = manager_root
        self.manager_root.title("T A X I - B O O K I N G - S Y S T E M")
        self.appearance_mode = "dark"
        self.screen_width = self.manager_root.winfo_screenwidth()
        self.screen_height = self.manager_root.winfo_screenheight()
        self.geometry()
        self.connection = Storage.Connect()
        self.managerFrontend()
   
    def geometry(self):
        screen_width = self.manager_root.winfo_screenwidth()
        screen_height = self.manager_root.winfo_screenheight()
        self.manager_root.geometry(f'{screen_width}x{screen_height}')
    
    def user_profile(self):
       
       self.new_popup = customtkinter.CTkToplevel(self.manager_root)
       self.new_popup.title("M A N A G E R -  P R O F I L E")
       self.new_popup.geometry('350x260')

       self.fullName = customtkinter.CTkLabel(self.new_popup, text="Full Name:", font=('calibri', 18, 'bold'), width=120)
       self.fullName.place(x=10, y=10)

       full_name_text = f"{gobal.manager[1]}"
       self.fullNameEn = customtkinter.CTkLabel(self.new_popup, text=full_name_text, font=('calibri', 18, 'bold'))
       self.fullNameEn.place(x=140, y=10)

       self.age = customtkinter.CTkLabel(self.new_popup, text="Age:", font=('calibri', 18, 'bold'), width=120)
       self.age.place(x=10, y=40)
    
       self.ageen = customtkinter.CTkLabel(self.new_popup, text=gobal.manager[4], font=('calibri', 18, 'bold'))
       self.ageen.place(x=140, y=40)
    
       self.ADDRESS = customtkinter.CTkLabel(self.new_popup, text="Phone:", font=('calibri', 18, 'bold'), width=120)
       self.ADDRESS.place(x=10, y=130)
    
       self.add = customtkinter.CTkLabel(self.new_popup, text=gobal.manager[6], font=('calibri', 18, 'bold'))
       self.add.place(x=140, y=130)

       self.pn = customtkinter.CTkLabel(self.new_popup, text="Country:", font=('calibri', 18, 'bold'), width=120)
       self.pn.place(x=10, y=160)
    
       self.pen = customtkinter.CTkLabel(self.new_popup, text=gobal.manager[5], font=('calibri', 18, 'bold'))
       self.pen.place(x=140, y=160)
       self.email = customtkinter.CTkLabel(self.new_popup, text="Email:", font=('calibri', 18, 'bold'), width=120)
       self.email.place(x=10, y=190)
    
       self.em = customtkinter.CTkLabel(self.new_popup, text=gobal.manager[2], font=('calibri', 18, 'bold'))
       self.em.place(x=140, y=190)
       self.passcode = customtkinter.CTkLabel(self.new_popup, text="Password:", font=('calibri', 18, 'bold'), width=120)
       self.passcode.place(x=10, y=220)
    
       self.pw = customtkinter.CTkLabel(self.new_popup, text=gobal.manager[3], font=('calibri', 18, 'bold'))
       self.pw.place(x=140, y=220)
       window_width = self.manager_root.winfo_screenwidth()
       self.new_popup.geometry(f'+{window_width - 300}+0')
       self.new_popup.resizable(False, False)
       self.new_popup.attributes('-topmost', 'true')
       self.new_popup.lift()
    def managerFrontend(self):
       upper_panel=customtkinter.CTkFrame(self.manager_root,width=230,height=100,fg_color="skyblue").place(x=0,y=0)
       self.UpperPanel(upper_panel)
       left_panel=customtkinter.CTkFrame(self.manager_root,width=230,height=self.screen_height)
       left_panel.place(x=0,y=110)
       self.logout=customtkinter.CTkButton(left_panel,text='Logout',command=self.log_out)
       self.logout.place(x=10,y=570)
        
       self.left(left_panel)
       title_panel = customtkinter.CTkFrame(self.manager_root, width=self.screen_width, height=100, fg_color="#05695A").place(x=240, y=0)
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
       first_box=customtkinter.CTkFrame(self.manager_root,width=320,height=160)
       first_box.place(x=240,y=110)
       self.first=customtkinter.CTkButton(first_box,width=320,text=" Customers",height=160,fg_color='#04473D',image=user_wid, compound=tk.TOP,text_color='black',font=("league spartan", 20, 'bold') ,command=lambda: self.switch_tab("CUSTOMERS"))
       self.first.place(x=0,y=0)
       second_box=customtkinter.CTkFrame(self.manager_root,width=320,height=160)
       second_box.place(x=570,y=110)
       self.second=customtkinter.CTkButton(second_box,text=" Booked Rides",width=320,height=160,image=user_ride_wid, compound=tk.TOP,fg_color='#04473D',text_color='black',font=("league spartan", 20, 'bold'), command=lambda: self.switch_tab("BOOKING"))
       self.second.place(x=0,y=0)
       third_box=customtkinter.CTkFrame(self.manager_root,width=320,height=160)
       third_box.place(x=900,y=110)
       self.third=customtkinter.CTkButton(third_box,text="Active Drivers",width=320,height=160,image=user_drover, compound=tk.TOP,fg_color="#04473D",text_color='black',font=("league spartan", 20, 'bold'), command=lambda: self.switch_tab("ACTIVE DRIVERS"))
       self.third.place(x=0,y=0)
       fourth_box=customtkinter.CTkFrame(self.manager_root,width=293,height=160)
       fourth_box.place(x=1230,y=110)
       self.fourth=customtkinter.CTkButton(fourth_box,text="Inactive Drivers",width=320,image=inactive_wid, compound=tk.TOP,height=160,fg_color="#04473D",text_color='black',font=("league spartan", 20, 'bold'), command=lambda: self.switch_tab("INACTIVE DRIVERS"))
       self.fourth.place(x=0,y=0)

       tabs=customtkinter.CTkTabview(self.manager_root,width=1265,height=500,fg_color="#A9C487",anchor='nw',text_color='white',segmented_button_fg_color="black",segmented_button_unselected_hover_color='skyblue',segmented_button_unselected_color='black',segmented_button_selected_color='#A9C487',segmented_button_selected_hover_color="skyblue")
       tabs.place(x=240,y=280)

       self.tabs = tabs 
       tabs.add("CUSTOMERS")
       self.customers(tabs.tab("CUSTOMERS"))
       tabs.add("BOOKING")
       tabs.add("ACTIVE DRIVERS")
       self.activated(tabs.tab("ACTIVE DRIVERS"))
       tabs.add("INACTIVE DRIVERS")
       self.deactivate(tabs.tab("INACTIVE DRIVERS"))
       tabs.add("CUSTOMER RATING")

       tabs2=customtkinter.CTkTabview(tabs.tab("BOOKING"),width=1265,height=400,fg_color="#A9C487",anchor='nw',text_color='white',segmented_button_fg_color="black",segmented_button_unselected_hover_color='skyblue',segmented_button_unselected_color='black',segmented_button_selected_color='#A9C487',segmented_button_selected_hover_color="skyblue")
       tabs2.place(x=5,y=4)
      
       self.tabs2 = tabs2
       tabs2.add("All Bookings")
       self.book(tabs2.tab("All Bookings"))
       tabs2.add("Requested Booking")
       self.request(tabs2.tab("Requested Booking"))
       tabs2.add("Accepted Booking")
       self.accepted(tabs2.tab("Accepted Booking"))
       tabs2.add("Completed Booking")
       self.completed(tabs2.tab("Completed Booking"))
    def delete_ACTIVE_click(self):
        selected_item = self.ac_booking.selection()
        if selected_item:
            driver_id = self.ac_booking.item(selected_item)['values'][0]
        
            self.update_status(driver_id, 'deleted')
            messagebox.showinfo("Deleted", "Driver Deleted Successfully")
            self.view_active()
        else:
            messagebox.showerror("Invalid deletion", "Please select a row to Delete")
    def deactivate(self,up):
        self.search=customtkinter.CTkEntry(up,font=("league spartan", 12, 'bold'),placeholder_text="Search",width=200)
        self.search.place(x=10,y=3)
        self.se=customtkinter.CTkButton(up,text="Search",width=80,font=("league spartan", 12, 'bold'))
        self.se.place(x=220,y=3)
        self.reg=customtkinter.CTkButton(up, text="Register", font=("league spartan", 12, 'bold'), command=lambda: self.register_button_click())

        self.reg.place(x=948,y=3)
        self.regis=customtkinter.CTkButton(up,text="Delete",font=("league spartan", 12, 'bold'),command=self.delete_button_click)
        self.regis.place(x=1094,y=3)
        column = ("Driver id","First Name", "Last Name","Age","Gender","Date of Birth","Country",'Phone Number','Email','Password','license','experience','status')
        self.in_booking = ttk.Treeview(up, columns=column, show="headings", height=24)

        for col in column:
            self.in_booking.heading(col, text=col, anchor="center")
            self.in_booking.column(col, anchor="center",width=119)
       
        
        self.view_deactive()
        self.in_booking.place(x=5,y=50)
    def view_deactive(self):
        try:
           with self.connection.cursor() as cursor:
            query = f"SELECT `driver_id`, `fname`, `lname`, `age`, `gender`, `dateofBirth`, `country`, `pno`, `email`, `passcode`, `license`, `experience`, `status` FROM `driver_registration` WHERE status='inactive' "

            cursor.execute(query)
            rows = cursor.fetchall()

            for item in self.in_booking.get_children():  # Corrected reference to self.in_booking
                self.in_booking.delete(item)  # Corrected reference to self.in_booking

            for row in rows:
                self.in_booking.insert(parent='', index='end', values=(row[0], row[1], row[2], row[3], row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12]))
        except Exception as err:
         print(f"Error: {err}")
    def delete_button_click(self):
        selected_item = self.in_booking.selection()
        if selected_item:
            driver_id = self.in_booking.item(selected_item)['values'][0]
            print(driver_id)
            self.update_status(driver_id, 'deleted')
            messagebox.showinfo("Deleted", "Driver Deleted Successfully")
            self.view_deactive()
        else:
            messagebox.showerror("Invalid deletion", "Please select a row to Delete")
    def register_button_click(self):
        selected_item = self.in_booking.selection()
        if selected_item:
           driver_id = self.in_booking.item(selected_item)['values'][0]
           print(driver_id)
           self.update_status(driver_id, 'active')
           messagebox.showinfo("Registered", "Driver Registerd Successfully")
           self.view_deactive()
           self.view_active()
        else:
            messagebox.showerror("Invalid registration", "Please select a row to Register")
    def update_status(self, driver_id, new_status):
        try:
            with self.connection.cursor() as cursor:
               query = f"UPDATE `driver_registration` SET `status` = %s WHERE `driver_id` = %s"
               cursor.execute(query, (new_status, driver_id))
               self.connection.commit()
               self.view_deactive()
               self.view_active()
        except Exception as err:
            print(f"Error updating status: {err}")


    def activated(self,up):
        self.search=customtkinter.CTkEntry(up,font=("league spartan", 12, 'bold'),placeholder_text="Search",width=200)
        self.search.place(x=10,y=3)
        self.se=customtkinter.CTkButton(up,text="Search",width=80,font=("league spartan", 12, 'bold'))
        self.se.place(x=220,y=3)
        self.update=customtkinter.CTkButton(up,text="Deactivate",font=("league spartan", 12, 'bold'),command=lambda:self.updateClick())
        self.update.place(x=948,y=3)
        self.regis=customtkinter.CTkButton(up,text="Delete",font=("league spartan", 12, 'bold'),command=self.delete_ACTIVE_click)
        self.regis.place(x=1094,y=3)
        column = ("Driver id","First Name", "Last Name","Age","Gender","Date of Birth","Country",'Phone Number','Email','Password','license','experience','status')
        self.ac_booking = ttk.Treeview(up, columns=column, show="headings", height=24)

        for col in column:
            self.ac_booking.heading(col, text=col, anchor="center")
            self.ac_booking.column(col, anchor="center",width=119)
       
        
        self.view_active()
        self.ac_booking.place(x=5,y=50)
    def view_active(self):
        try:
            with self.connection.cursor() as cursor:
                query = f"SELECT `driver_id`, `fname`, `lname`, `age`, `gender`, `dateofBirth`, `country`, `pno`, `email`, `passcode`, `license`, `experience`, `status` FROM `driver_registration` WHERE status='active' "

                cursor.execute(query)
                rows = cursor.fetchall()

                for item in self.ac_booking.get_children():
                    self.ac_booking.delete(item)

                for row in rows:
                    self.ac_booking.insert(parent='', index='end', values=(row[0], row[1], row[2], row[3], row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12]))
        except Exception as err:
            print(f"Error: {err}")
    def updateClick(self):
        selected_item = self.ac_booking.selection()
        if selected_item:
           driver_id = self.ac_booking.item(selected_item)['values'][0]
           print(driver_id)
           self.updateStatus(driver_id, 'inactive')
           messagebox.showinfo("Success", "Driver inactive Successfully")
           self.view_active()
           self.view_Active()
        else:
            messagebox.showerror("Invalid ", "Please select a row to make inactive")
    def updateStatus(self, driver_id, new_status):
        try:
            with self.connection.cursor() as cursor:
               query = f"UPDATE `driver_registration` SET `status` = %s WHERE `driver_id` = %s"
               cursor.execute(query, (new_status, driver_id))
               self.connection.commit()
               self.view_deactive()
        except Exception as err:
            print(f"Error updating status: {err}")

    def customers(self,up):
        
        self.search=customtkinter.CTkEntry(up,font=("league spartan", 12, 'bold'),placeholder_text="Search",width=200)
        self.search.place(x=10,y=3)
        self.se=customtkinter.CTkButton(up,text="Search",width=80,font=("league spartan", 12, 'bold'))
        self.se.place(x=220,y=3)
        self.delete=customtkinter.CTkButton(up,text="Delete",font=("league spartan", 12, 'bold'),command=self.delete_customer_click)
        self.delete.place(x=1098,y=3)
        column = ("customer_id","First Name", "Last Name","Age","Gender","Date of Birth",'Phone Number','Country','Email','Password')
        self.de_booking = ttk.Treeview(up, columns=column, show="headings", height=24)

        for col in column:
            self.de_booking.heading(col, text=col, anchor="center")
            self.de_booking.column(col, anchor="center",width=155)
       
        
        self.view_bookings()
        self.de_booking.place(x=5,y=50)
    def delete_customer_click(self):
        selected_item = self.de_booking.selection()
        if selected_item:
            customer_id = self.de_booking.item(selected_item)['values'][0]

            try:
              with self.connection.cursor() as cursor:
             
                query = f"DELETE FROM `customer_registration` WHERE `customer_id` = {customer_id}"
                cursor.execute(query)
                self.connection.commit()

                messagebox.showinfo("Deleted", "Customer Deleted Successfully")
            
                self.de_booking.delete(selected_item)

            except Exception as err:
             print(f"Error: {err}")
        else:
          messagebox.showerror("Invalid deletion", "Please select a row to Delete")

    def view_bookings(self):
        try:
            with self.connection.cursor() as cursor:
                query = f"SELECT `customer_id`, `firstName`, `lastName`, `age`, `gender`, `dateOfBirth`, `phone`, `country`, `email`, `password` FROM `customer_registration`"
                cursor.execute(query)
                rows = cursor.fetchall()

                for item in self.de_booking.get_children():
                    self.de_booking.delete(item)

                for row in rows:
                    self.de_booking.insert(parent='', index='end', values=(row[0], row[1], row[2], row[3], row[4],row[5],row[6],row[7],row[8],row[9]))
        except Exception as err:
            print(f"Error: {err}")
    def book(self,book_table):
        self.search=customtkinter.CTkEntry(book_table,font=("league spartan", 12, 'bold'),placeholder_text="Search",width=200)
        self.search.place(x=10,y=3)
        self.se=customtkinter.CTkButton(book_table,text="Search",width=80,font=("league spartan", 12, 'bold'))
        self.se.place(x=220,y=3)
        self.delete=customtkinter.CTkButton(book_table,text="Delete",font=("league spartan", 12, 'bold'))
        self.delete.place(x=1094,y=3)
        column = ("Booking Id","Customer ID","Customer Name","Location", "Destination","Time","Date","Status")
        self.tree_booking = ttk.Treeview(book_table, columns=column, show="headings", height=36)

        for col in column:
            self.tree_booking.heading(col, text=col, anchor="center")
            self.tree_booking.column(col, anchor="center",width=190)
       
        
        self.bookings()
        self.tree_booking.place(x=10,y=50)
    def bookings(self):
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
    def request(self,req_table):
        self.search=customtkinter.CTkEntry(req_table,font=("league spartan", 12, 'bold'),placeholder_text="Search",width=200)
        self.search.place(x=10,y=3)
        self.se=customtkinter.CTkButton(req_table,text="Search",width=80,font=("league spartan", 12, 'bold'))
        self.se.place(x=220,y=3)
        self.delete=customtkinter.CTkButton(req_table,text="Delete",font=("league spartan", 12, 'bold'))
        self.delete.place(x=1094,y=3)
        column = ("Booking Id","Customer ID","Customer Name","Location", "Destination","Time","Date","Status")
        self.tree_booking = ttk.Treeview(req_table, columns=column, show="headings", height=20)

        for col in column:
            self.tree_booking.heading(col, text=col, anchor="center")
            self.tree_booking.column(col, anchor="center",width=190)
       
        
        self.req_book()
        self.tree_booking.place(x=10,y=50)
    def req_book(self):
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
    customer_registration ON reservation.customer_id = customer_registration.customer_id
WHERE 
    reservation.status = 'pending';


"""
                cursor.execute(query)
                rows = cursor.fetchall()

                for item in self.tree_booking.get_children():
                    self.tree_booking.delete(item)

                for row in rows:
                    self.tree_booking.insert(parent='', index='end', values=(row[0], row[1], row[2], row[3], row[4],row[5],row[6],row[7]))
        except Exception as err:
            print(f"Error: {err}")

    def completed(self,comp):
        self.search=customtkinter.CTkEntry(comp,font=("league spartan", 12, 'bold'),placeholder_text="Search",width=200)
        self.search.place(x=10,y=3)
        self.se=customtkinter.CTkButton(comp,text="Search",width=80,font=("league spartan", 12, 'bold'))
        self.se.place(x=220,y=3)
        self.delete=customtkinter.CTkButton(comp,text="Delete",font=("league spartan", 12, 'bold'))
        self.delete.place(x=1094,y=3)
        column = ("Booking Id","Customer ID","Customer Name","Location", "Destination","Time","Date","Status")
        self.tree_booking = ttk.Treeview(comp, columns=column, show="headings", height=20)

        for col in column:
            self.tree_booking.heading(col, text=col, anchor="center")
            self.tree_booking.column(col, anchor="center",width=190)
       
        
        self.com_book()
        self.tree_booking.place(x=10,y=50)
    def com_book(self):
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
    customer_registration ON reservation.customer_id = customer_registration.customer_id
WHERE 
    reservation.status = 'completed';


"""
                cursor.execute(query)
                rows = cursor.fetchall()

                for item in self.tree_booking.get_children():
                    self.tree_booking.delete(item)

                for row in rows:
                    self.tree_booking.insert(parent='', index='end', values=(row[0], row[1], row[2], row[3], row[4],row[5],row[6],row[7]))
        except Exception as err:
            print(f"Error: {err}")
    def accepted(self,accept):
        self.search=customtkinter.CTkEntry(accept,font=("league spartan", 12, 'bold'),placeholder_text="Search",width=200)
        self.search.place(x=10,y=3)
        self.se=customtkinter.CTkButton(accept,text="Search",width=80,font=("league spartan", 12, 'bold'))
        self.se.place(x=220,y=3)
        self.delete=customtkinter.CTkButton(accept,text="Delete",font=("league spartan", 12, 'bold'))
        self.delete.place(x=1094,y=3)
        column = ("Booking Id","Customer ID","Customer Name","Location", "Destination","Time","Date","Status")
        self.tree_booking = ttk.Treeview(accept, columns=column, show="headings", height=20)

        for col in column:
            self.tree_booking.heading(col, text=col, anchor="center")
            self.tree_booking.column(col, anchor="center",width=190)
       
        
        self.acc_book()
        self.tree_booking.place(x=10,y=50)
    def acc_book(self):
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
    customer_registration ON reservation.customer_id = customer_registration.customer_id
WHERE 
    reservation.status = 'accepted';


"""
                cursor.execute(query)
                rows = cursor.fetchall()

                for item in self.tree_booking.get_children():
                    self.tree_booking.delete(item)

                for row in rows:
                    self.tree_booking.insert(parent='', index='end', values=(row[0], row[1], row[2], row[3], row[4],row[5],row[6],row[7]))
        except Exception as err:
            print(f"Error: {err}")
    def UpperPanel(self,up):
           taxi_label=customtkinter.CTkLabel(up,text="T A X I ",font=("league spartan",30,'bold'),text_color='black',bg_color='skyblue').place(x=55,y=2)
           sys_label=customtkinter.CTkLabel(up,text="S Y S T E M",font=("league spartan",30,'bold'),text_color='black',bg_color='skyblue').place(x=26,y=44)
           
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

    def switch_tab(self, tab_name):
        self.tabs.set(tab_name)   
    def left(self,bloom):
       path = os.path.join(os.path.dirname(__file__), r"D:\Desktop\Taxi Booking System\assets\man.png")
       pathimage = PILImage.open(path)
       user_p= customtkinter.CTkImage(dark_image=pathimage, light_image=pathimage, size=(200, 190))  
       mail_label = customtkinter.CTkLabel(bloom, text=None, image=user_p)
       mail_label.place(x=10, y=20)
       full_name=customtkinter.CTkLabel(bloom, text="FULL NAME ", font=('calibri', 18, 'bold'))
       full_name.place(x=10,y=240)
       fn=customtkinter.CTkLabel(bloom, text=gobal.manager[1], font=('calibri', 18, 'bold'))
       fn.place(x=10,y=270)
       age=customtkinter.CTkLabel(bloom, text="AGE ", font=('calibri', 18, 'bold'))
       age.place(x=10,y=310)
       an=customtkinter.CTkLabel(bloom, text=gobal.manager[4], font=('calibri', 18, 'bold'))
       an.place(x=10,y=340)
       pn=customtkinter.CTkLabel(bloom, text="PHONE ", font=('calibri', 18, 'bold'))
       pn.place(x=10,y=380)
       phone=customtkinter.CTkLabel(bloom, text=gobal.manager[5], font=('calibri', 18, 'bold'))
       phone.place(x=10,y=410)
       add=customtkinter.CTkLabel(bloom, text="ADDRESS ", font=('calibri', 18, 'bold'))
       add.place(x=10,y=440)
       fadren=customtkinter.CTkLabel(bloom, text=gobal.manager[6], font=('calibri', 18, 'bold'))
       fadren.place(x=10,y=470)
       email=customtkinter.CTkLabel(bloom, text="EMAIL", font=('calibri', 18, 'bold'))
       email.place(x=10,y=510)
       em=customtkinter.CTkLabel(bloom, text=gobal.manager[2], font=('calibri', 18, 'bold'))
       em.place(x=10,y=540)

      
    def log_out(self):
        self.manager_root.destroy()
        dash_win = customtkinter.CTk()
        from login_form import LoginUser
        dash_app = LoginUser(dash_win)
        dash_win.after(0,lambda:dash_win.state('zoomed'))
        dash_win.mainloop()

if __name__ == "__main__":
    manager_root = customtkinter.CTk()
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue") 
    manager_root.after(0,lambda:manager_root.state('zoomed'))
    user_dash = Dashboard(manager_root)
    manager_root.mainloop()
 

     
        
       

   
       



