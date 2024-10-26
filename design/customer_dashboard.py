import os
import sys

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
    def __init__(self, window):
        self.window = window
        self.window.title("T A X I - B O O K I N G - S Y S T E M")
        self.appearance_mode = "dark"
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()
        self.geometry()
        self.connection = Storage.Connect()
        self.frontend()
   
    def geometry(self):
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.window.geometry(f'{screen_width}x{screen_height}')
    
    def user_profile(self):
       self.new_popup = customtkinter.CTkToplevel(self.window)
       self.new_popup.title("U S E R  -  P R O F I L E")
       self.new_popup.geometry('240x260')

       self.fullName = customtkinter.CTkLabel(self.new_popup, text="Full Name:", font=('calibri', 18, 'bold'), width=120)
       self.fullName.place(x=10, y=10)

       full_name_text = f"{gobal.customer[1]} {gobal.customer[2]}"
       self.fullNameEn = customtkinter.CTkLabel(self.new_popup, text=full_name_text, font=('calibri', 18, 'bold'))
       self.fullNameEn.place(x=140, y=10)

       self.age = customtkinter.CTkLabel(self.new_popup, text="Age:", font=('calibri', 18, 'bold'), width=120)
       self.age.place(x=10, y=40)
    
       self.ageen = customtkinter.CTkLabel(self.new_popup, text=gobal.customer[3], font=('calibri', 18, 'bold'))
       self.ageen.place(x=140, y=40)

       self.gender = customtkinter.CTkLabel(self.new_popup, text="Gender:", font=('calibri', 18, 'bold'), width=120)
       self.gender.place(x=10, y=70)
    
       self.gen = customtkinter.CTkLabel(self.new_popup, text=gobal.customer[4], font=('calibri', 18, 'bold'))
       self.gen.place(x=140, y=70)

    
       self.dob = customtkinter.CTkLabel(self.new_popup, text="Date of Birth:", font=('calibri', 18, 'bold'), width=120)
       self.dob.place(x=10, y=100)
    
       self.doben = customtkinter.CTkLabel(self.new_popup, text=gobal.customer[5], font=('calibri', 18, 'bold'))
       self.doben.place(x=140, y=100)

       self.country = customtkinter.CTkLabel(self.new_popup, text="Phone:", font=('calibri', 18, 'bold'), width=120)
       self.country.place(x=10, y=130)
    
       self.cou = customtkinter.CTkLabel(self.new_popup, text=gobal.customer[6], font=('calibri', 18, 'bold'))
       self.cou.place(x=140, y=130)

       self.pn = customtkinter.CTkLabel(self.new_popup, text="Country:", font=('calibri', 18, 'bold'), width=120)
       self.pn.place(x=10, y=160)
    
       self.pen = customtkinter.CTkLabel(self.new_popup, text=gobal.customer[7], font=('calibri', 18, 'bold'))
       self.pen.place(x=140, y=160)
       self.email = customtkinter.CTkLabel(self.new_popup, text="Email:", font=('calibri', 18, 'bold'), width=120)
       self.email.place(x=10, y=190)
    
       self.em = customtkinter.CTkLabel(self.new_popup, text=gobal.customer[8], font=('calibri', 18, 'bold'))
       self.em.place(x=140, y=190)
       self.passcode = customtkinter.CTkLabel(self.new_popup, text="Password:", font=('calibri', 18, 'bold'), width=120)
       self.passcode.place(x=10, y=220)
    
       self.pw = customtkinter.CTkLabel(self.new_popup, text=gobal.customer[8], font=('calibri', 18, 'bold'))
       self.pw.place(x=140, y=220)
       window_width = self.window.winfo_screenwidth()
       self.new_popup.geometry(f'+{window_width - 300}+0')
       self.new_popup.resizable(False, False)
       self.new_popup.attributes('-topmost', 'true')
       self.new_popup.lift()


    def frontend(self):
        navbar = customtkinter.CTkFrame(self.window, width=self.screen_width, height=45)
        navbar.place(x=0, y=0)
        
        logo_path = os.path.join(os.path.dirname(__file__), r"D:\Desktop\Taxi Booking System\assets\logo.png")
        bell_path = os.path.join(os.path.dirname(__file__), r"D:\Desktop\Taxi Booking System\assets\bell.png")
        mail_path = os.path.join(os.path.dirname(__file__), r"D:\Desktop\Taxi Booking System\assets\mail.png")
        nepal_path = os.path.join(os.path.dirname(__file__), r"D:\Desktop\Taxi Booking System\assets\nepal.png")
        user_dash=os.path.join(os.path.dirname(__file__), r"D:\Desktop\Taxi Booking System\assets\user_table.png")
        tap=os.path.join(os.path.dirname(__file__), r"D:\Desktop\Taxi Booking System\assets\tap.png")
        book=os.path.join(os.path.dirname(__file__), r"D:\Desktop\Taxi Booking System\assets\book.png")
        ride=os.path.join(os.path.dirname(__file__), r"D:\Desktop\Taxi Booking System\assets\ride.png")
        order=os.path.join(os.path.dirname(__file__), r"D:\Desktop\Taxi Booking System\assets\order.png")
        rating=os.path.join(os.path.dirname(__file__), r"D:\Desktop\Taxi Booking System\assets\rating.png")
        logo_image = PILImage.open(logo_path)
        bell_image = PILImage.open(bell_path)
        mail_image = PILImage.open(mail_path)
        nepal_image = PILImage.open(nepal_path)
        tap_image=PILImage.open(tap)
        book_image=PILImage.open(book)
        ride_image=PILImage.open(ride)
        order_image=PILImage.open(order)
        rating_image=PILImage.open(rating)
        user_Dash_img=PILImage.open(user_dash)
        
        logo_widget = customtkinter.CTkImage(dark_image=logo_image, light_image=logo_image, size=(55, 50))
        logo_label = customtkinter.CTkLabel(navbar, text=None, image=logo_widget)
        logo_label.place(x=5, y=0)

        bell_widget = customtkinter.CTkImage(dark_image=bell_image, light_image=bell_image, size=(33, 33))
        bell_label = customtkinter.CTkLabel(navbar, text=None, image=bell_widget)
        bell_label.place(x=1250, y=9)

        mail_widget = customtkinter.CTkImage(dark_image=mail_image, light_image=mail_image, size=(50, 35))
        mail_label = customtkinter.CTkLabel(navbar, text=None, image=mail_widget)
        mail_label.place(x=1280, y=6)

        nepal_widget = customtkinter.CTkImage(dark_image=nepal_image, light_image=nepal_image, size=(50, 33))
        nepal_label = customtkinter.CTkLabel(navbar, text=None, image=nepal_widget)
        nepal_label.place(x=1320, y=6)

        switch_one = customtkinter.StringVar(value='on')
        def toggle_mode():
            if switch_one.get() == 'on':
                customtkinter.set_appearance_mode("dark")
            else:
                customtkinter.set_appearance_mode("light")
              
        toggle = customtkinter.CTkSwitch(navbar, text=None, command=toggle_mode, variable=switch_one, onvalue='on', offvalue='off')
        toggle.place(x=1360, y=6)

        name_label=customtkinter.CTkButton(navbar,text="PROFILE",font=('calibri',16,'bold'),width=120,command=self.user_profile)
        name_label.place(x=1410,y=9)
        date = dt.datetime.now()
        format_date = f"{date:%a, %b %d %Y}"
        entry = customtkinter.CTkEntry(navbar, width=130, font=("Calibri", 15))
        entry.insert(END, format_date)
        entry.place(x=50, y=10)

        #---------------- ---------- 
        upper_panel=customtkinter.CTkFrame(self.window,width=self.screen_width, height=120,fg_color='#100D03')  
        upper_panel.place(x=0,y=46)
        self.left_panel = customtkinter.CTkFrame(self.window, width=220, height=self.screen_height, fg_color="#100D03",bg_color="#201E1E")
        full_name=customtkinter.CTkLabel( self.left_panel, text="FULL NAME ", font=('calibri', 18, 'bold'))
        full_name.place(x=10,y=20)
        fn=customtkinter.CTkLabel( self.left_panel, text=f'{gobal.customer[1]},{gobal.customer[2]}', font=('calibri', 18, 'bold'))
        fn.place(x=10,y=50)

        age=customtkinter.CTkLabel( self.left_panel, text="AGE ", font=('calibri', 18, 'bold'))
        age.place(x=10,y=90)
        an=customtkinter.CTkLabel( self.left_panel, text=gobal.customer[3], font=('calibri', 18, 'bold'))
        an.place(x=10,y=120)

        pn=customtkinter.CTkLabel( self.left_panel, text="PHONE ", font=('calibri', 18, 'bold'))
        pn.place(x=10,y=160)
        phone=customtkinter.CTkLabel( self.left_panel, text=gobal.customer[6], font=('calibri', 18, 'bold'))
        phone.place(x=10,y=190)

        add=customtkinter.CTkLabel( self.left_panel, text="GENDER ", font=('calibri', 18, 'bold'))
        add.place(x=10,y=230)
        fadren=customtkinter.CTkLabel( self.left_panel, text=gobal.customer[4], font=('calibri', 18, 'bold'))
        fadren.place(x=10,y=260)
        email=customtkinter.CTkLabel( self.left_panel, text="DATE OF BIRTH", font=('calibri', 18, 'bold'))
        email.place(x=10,y=300)
        em=customtkinter.CTkLabel( self.left_panel, text=gobal.customer[5], font=('calibri', 18, 'bold'))
        em.place(x=10,y=330)

        COUNTRY=customtkinter.CTkLabel( self.left_panel, text="COUNTRY ", font=('calibri', 18, 'bold'))
        COUNTRY.place(x=10,y=370)
        coun=customtkinter.CTkLabel( self.left_panel, text=gobal.customer[7], font=('calibri', 18, 'bold'))
        coun.place(x=10,y=400)
        username=customtkinter.CTkLabel( self.left_panel, text="DATE OF BIRTH", font=('calibri', 18, 'bold'))
        username.place(x=10,y=440)
        userem=customtkinter.CTkLabel( self.left_panel, text=gobal.customer[5], font=('calibri', 18, 'bold'))
        userem.place(x=10,y=470)

        passw=customtkinter.CTkLabel( self.left_panel, text="COUNTRY ", font=('calibri', 18, 'bold'))
        passw.place(x=10,y=510)
        pcode=customtkinter.CTkLabel( self.left_panel, text=gobal.customer[7], font=('calibri', 18, 'bold'))
        pcode.place(x=10,y=540)
        self.left_panel.place(x=0,y=166)
        self.logout=customtkinter.CTkButton(self.left_panel,text='Logout',command=self.log_out)
        self.logout.place(x=10,y=570)
        
        welcome_label=customtkinter.CTkLabel(upper_panel,text="WELCOME TO THE DASHBOARD",bg_color="transparent",font=("calibri",55,'bold'))
        welcome_label.place(x=340,y=25)         
        mr_label=customtkinter.CTkLabel(upper_panel,text='',bg_color="transparent",font=("calibri",55,'bold'))
        mr_label.configure(text=f'Mr.{gobal.customer[1]}')
        mr_label.place(x=1200,y=25)
        user_dash_widget = customtkinter.CTkImage(dark_image=user_Dash_img, light_image=user_Dash_img, size=(180, 130))
        dash_label = customtkinter.CTkLabel(upper_panel, text=None, image=user_dash_widget)
        dash_label.place(x=20, y=0)
        tabs=customtkinter.CTkTabview(self.window,width=1265,height=605,fg_color="#A9C487",anchor='nw',text_color='white',segmented_button_fg_color="black",segmented_button_unselected_hover_color='skyblue',segmented_button_unselected_color='black',segmented_button_selected_color='#A9C487',segmented_button_selected_hover_color="skyblue")
        tabs.place(x=240,y=170)

        self.tabs = tabs 
        tabs.add("HOME")
        tabs.add("BOOKING")
        tabs.add("MY RIDES")
        tabs.add("PAYMENT")
        tabs.add("CUSTOMER RATING")
        self.payment(tabs.tab("PAYMENT"))
       

        sub_frame = customtkinter.CTkFrame(tabs.tab("HOME"), width=880, height=240)
        sub_frame.place(x=10, y=10)
        book_widget = customtkinter.CTkImage(dark_image=book_image, light_image=book_image, size=(25, 25))
        tap_widget = customtkinter.CTkImage(dark_image=tap_image, light_image=tap_image, size=(880, 240))
        tap_Label = customtkinter.CTkLabel(sub_frame, text=None, image=tap_widget)
        tap_Label.place(x=0, y=0)
        book_button = customtkinter.CTkButton(sub_frame, text='Book a Cab Instantly', font=('helvetica', 20, "bold"), fg_color="transparent", hover_color='green', corner_radius=10, image=book_widget, compound='right', command=lambda: self.switch_tab("BOOKING"))
        book_button.place(x=600, y=200)


        sub_frame2 = customtkinter.CTkFrame(tabs.tab("HOME"), width=330, height=550)
        ride_widget = customtkinter.CTkImage(dark_image=ride_image, light_image=ride_image, size=(330, 550))
        ride_label = customtkinter.CTkLabel(sub_frame2, text=None, image=ride_widget)
        ride_button=customtkinter.CTkButton(sub_frame2,text='VIEW RIDES',font=('helvetica',20,"bold"),fg_color="transparent",hover_color='skyblue',corner_radius=10,image=book_widget,compound='right',command=lambda: self.switch_tab("MY RIDES"))
        ride_button.place(x=100,y=450)

        ride_label.place(x=0, y=0)

        sub_frame2.place(x=910, y=10) 
        sub_frame3 = customtkinter.CTkFrame(tabs.tab("HOME"), width=405, height=295)
        order_widget = customtkinter.CTkImage(dark_image=order_image, light_image=order_image, size=(405, 295))
        order_label = customtkinter.CTkLabel(sub_frame3, text=None, image=order_widget)
        order_label.place(x=0, y=0)
        order_btn=customtkinter.CTkButton(sub_frame3,text="ORDER NOW",fg_color="#FFFFCC",font=('helvetica',15,"bold"),text_color='black',hover_color='white')
        order_btn.place(x=120,y=244)
        sub_frame3.place(x=10, y=270)
        sub_frame4 = customtkinter.CTkFrame(tabs.tab("HOME"), width=450, height=295)
        rating_widget = customtkinter.CTkImage(dark_image=rating_image, light_image=rating_image, size=(450, 295))
        rating_label = customtkinter.CTkLabel(sub_frame4, text=None, image=rating_widget)
        rate_btn=customtkinter.CTkButton(sub_frame4,text="Rate Now",fg_color="white",font=('helvetica',15,"bold"),text_color='black',hover_color='blue')
        rate_btn.place(x=150,y=250)
        rating_label.place(x=0, y=0)
        sub_frame4.place(x=435, y=270)
        self.book_panel(tabs.tab("BOOKING"))
        self.view_panel(tabs.tab("MY RIDES"))
        self.book_btn=customtkinter.CTkButton(tabs.tab("BOOKING"),text='Request',fg_color="gray",font=('helvetica',15,"bold"),width=90,text_color='black',hover_color='skyblue',command=self.book)
        self.book_btn.place(x=1150,y=13)
        map_widget = tkintermapview.TkinterMapView(tabs.tab("BOOKING"), width=1500, height=680, corner_radius=0)
        map_widget.place(x=10,y=70)
    def log_out(self):
        self.window.destroy()
        dash_win = customtkinter.CTk()
        from login_form import LoginUser
        dash_app = LoginUser(dash_win)
        dash_win.after(0,lambda:dash_win.state('zoomed'))
        dash_win.mainloop()
    def delete_customer_click(self):
        selected_item = self.book_table_tree.selection()
        if selected_item:
            book_id = self.book_table_tree.item(selected_item)['values'][0]

            try:
              with self.connection.cursor() as cursor:
             
                query = f"DELETE FROM `reservation` WHERE `book_id` = {book_id}"
                cursor.execute(query)
                self.connection.commit()

                messagebox.showinfo("Deleted", "Booking Cancelled Successfully")
            
                self.book_table_tree.delete(selected_item)

            except Exception as err:
             print(f"Error: {err}")
        else:
          messagebox.showerror("Invalid deletion", "Please select a row to Delete")
    def update_book(self):
       selected_item = self.book_table_tree.selection()
       if selected_item:
        selected_item = selected_item[0] 
        try:
                with self.connection.cursor() as cursor:
                  book_id = self.book_table_tree.item(selected_item, 'values')[0]
                  new_location = self.pick_entry.get()
                  new_destination = self.dest_en.get()
                  new_date = self.en_dateee.get_date() 

                  query = f"UPDATE `reservation` SET `location` = %s, `destination` = %s, `date` = %s WHERE `book_id` = {book_id}"
                  cursor.execute(query, (new_location, new_destination, new_date))
                  self.connection.commit()
  
                  messagebox.showinfo("Updated", "Booking Updated Successfully")
                  self.book_table_tree.item(selected_item, values=(book_id, new_location, new_destination, '', new_date, ''))
                  self.view_bookings()
        except Exception as err:
                 print(f"Error: {err}")
       else:
        messagebox.showerror("Invalid update", "Please select a row to update")


    def view_panel(self,table):
        self.table_frame = ttk.Frame(table)
        self.table_frame.place(x=40, y=140)
        lb_pick_up=customtkinter.CTkLabel(table,text='Your Location :',bg_color="transparent",text_color='black',font=("calibri",18,'bold'))
        lb_pick_up.place(x=30,y=10)
        self.pick_entry=customtkinter.CTkEntry(table,placeholder_text="your current location",textvariable=StringVar(),width=225,height=35)
        self.pick_entry.place(x=160, y=7)
        self.dest=customtkinter.CTkLabel(table,text='Destination :',bg_color="transparent",text_color='black',font=("calibri",18,'bold'))
        self.dest.place(x=400,y=10)
        self.dest_en=customtkinter.CTkEntry(table,placeholder_text="Destination",textvariable=StringVar(),width=225,height=35)
        self.dest_en.place(x=510,y=7)
        self.selc_time=customtkinter.CTkLabel(table,text="Time :",bg_color="transparent",text_color='black',font=("calibri",18,'bold'))
        self.selc_time.place(x=750,y=7)
        
        self.datee=customtkinter.CTkLabel(table,text='Date :',bg_color="transparent",text_color='black',font=("calibri",18,'bold'))
        self.datee.place(x=1000,y=10)
        self.en_dateee = DateEntry(table, selectmode='day',width=12, background='darkblue', foreground='white', borderwidth=2)
        self.en_dateee.place(x=1320, y=20)
        self.search=customtkinter.CTkEntry(table,font=("league spartan", 12, 'bold'),placeholder_text="Search",width=200)
        self.search.place(x=40,y=70)
        self.se=customtkinter.CTkButton(table,text="Search",width=80,font=("league spartan", 12, 'bold'))
        self.se.place(x=260,y=70)
        self.edit=customtkinter.CTkButton(table,text='EDIT',font=('helvetica',15,"bold"),command=self.update_book)
        self.edit.place(x=890,y=70)
        self.cancel=customtkinter.CTkButton(table,text='CANCEL',font=('helvetica',15,"bold"),command=self.delete_customer_click)
        self.cancel.place(x=1050,y=70)
       
        self.digital_clock(table)
      
        column = ("Booking_id","Location", "Destination","time","date","status")
        self.book_table_tree = ttk.Treeview(self.table_frame, columns=column, show="headings", height=24)

        for col in column:
            self.book_table_tree.heading(col, text=col, anchor="center")
            self.book_table_tree.column(col, anchor="center",width=250)
        
       
        
        self.view_bookings()
        self.book_table_tree.pack()
       
      
    def view_bookings(self):
        self.cust_id=gobal.customer[0]
        try:
            with self.connection.cursor() as cursor:
                query = f"SELECT `book_id`, `location`, `destination`, `time`, `date`, `status` FROM `reservation` WHERE `customer_id` ={self.cust_id} "
                cursor.execute(query)
                rows = cursor.fetchall()

            for item in self.book_table_tree.get_children():
                self.book_table_tree.delete(item)

            for row in rows:
                self.book_table_tree.insert(parent='', index='end', values=(row[0], row[1], row[2], row[3], row[4],row[5]))

        except Exception as err:
            print(f"Error: {err}")


    def switch_tab(self, tab_name):
        self.tabs.set(tab_name)   
    def book_panel(self,book):
        pick_up=customtkinter.CTkLabel(book,text='Your Location :',bg_color="transparent",text_color='black',font=("calibri",18,'bold'))
        pick_up.place(x=30,y=10)
        self.pick_en=customtkinter.CTkEntry(book,placeholder_text="your current location",textvariable=StringVar(),width=225,height=35)
        self.pick_en.place(x=160,y=7)
        self.destination=customtkinter.CTkLabel(book,text='Destination :',bg_color="transparent",text_color='black',font=("calibri",18,'bold'))
        self.destination.place(x=400,y=10)
        self.destination_en=customtkinter.CTkEntry(book,placeholder_text="Destination",textvariable=StringVar(),width=225,height=35)
        self.destination_en.place(x=510,y=7)
        self.select_time=customtkinter.CTkLabel(book,text="Time :",bg_color="transparent",text_color='black',font=("calibri",18,'bold'))
        self.select_time.place(x=750,y=7)
        
        self.date=customtkinter.CTkLabel(book,text='Date :',bg_color="transparent",text_color='black',font=("calibri",18,'bold'))
        self.date.place(x=1000,y=10)
        self.en_dob = DateEntry(book, selectmode='day',width=12, background='darkblue', foreground='white', borderwidth=2)
        self.en_dob.place(x=1320, y=20)
       
        self.digital_clock(book)
    
    def digital_clock(self, frame):

       self.label_hours = customtkinter.CTkLabel(frame, text="-hr", bg_color="transparent", text_color='black', font=("calibri", 18, 'bold'))
       self.label_hours.place(x=840, y=8)
       self.spinbox_hours = Spinbox(frame, from_=1, to=12, width=5)
       self.spinbox_hours.place(x=1000, y=18) 

       self.label_minutes = customtkinter.CTkLabel(frame, text="-min:", bg_color="transparent", text_color='black', font=("calibri", 18, 'bold'))
       self.label_minutes.place(x=900, y=7)  # Adjusted x-coordinate
       self.spinbox_minutes = Spinbox(frame, from_=0, to=59, width=5)
       self.spinbox_minutes.place(x=1080, y=18)  # Adjusted x-coordinate

       self.spinbox_am_pm = Spinbox(frame, values=("AM", "PM"), width=5)
       self.spinbox_am_pm.place(x=1180, y=18)  # Adjusted x-coordinate


    def book(self):
       self.id=0
       self.customer_id=gobal.customer[0]
       location = self.pick_en.get()
       destination = self.destination_en.get()
       time = f'{self.spinbox_hours.get()}hr, {self.spinbox_minutes.get()}min, {self.spinbox_am_pm.get()}'
       date = self.en_dob.get_date()

       if not (location and destination and time and date):
        messagebox.showerror("Error", "Please fill in all fields.")
        return

       if location != '' and destination != '' and time != '' and date != '':
        booked = BookRide(self.id,location, destination, time, date,self.customer_id)
        book_store = RegisterStorage()
        success = book_store.ReserveRide(booked)

       if success:
            message = f"Ride requested successfully"
            self.view_bookings()
            messagebox.showinfo("Success", message)
       else:
            messagebox.showerror("Error", "Booking failed.")
    def payment(self,up):
         self.search=customtkinter.CTkEntry(up,font=("league spartan", 12, 'bold'),placeholder_text="Search",width=200)
         self.search.place(x=10,y=3)
         self.se=customtkinter.CTkButton(up,text="Search",width=80,font=("league spartan", 12, 'bold'))
         self.se.place(x=220,y=3)
         self.update=customtkinter.CTkButton(up,text="Accept",font=("league spartan", 12, 'bold'))
         self.update.place(x=948,y=3)
         self.regis=customtkinter.CTkButton(up,text="Cancel",font=("league spartan", 12, 'bold'))
         self.regis.place(x=1094,y=3)
         column = ("Customer Name","Driver Name", "Booking Id","location","Destination",'date','time',"status","pay_id",'price')
         self.ac_booking = ttk.Treeview(up, columns=column, show="headings", height=24)

         for col in column:
            self.ac_booking.heading(col, text=col, anchor="center")
            self.ac_booking.column(col, anchor="center",width=119)
       
        
         self.view_active()
         self.ac_booking.place(x=5,y=50)
    def view_active(self):
        try:
            with self.connection.cursor() as cursor:
                query = f"""
SELECT
    CONCAT(c.firstName, ' ', c.lastName) AS customer_name,
    CONCAT(d.fname, ' ', d.lname) AS driver_name,
    r.book_id,
    r.location,
    r.destination,
    r.date,
    r.time,
    r.status,
    p.pay_id,
    p.price
FROM
    reservation r
JOIN
    customer_registration c ON r.customer_id = c.customer_id
JOIN
    driver_registration d ON r.driver_id = d.driver_id
JOIN
    payment p ON r.pay_id = p.pay_id
WHERE 
r.status = 'accepted';
"""

                cursor.execute(query)
                rows = cursor.fetchall()

                for item in self.ac_booking.get_children():
                    self.ac_booking.delete(item)

                for row in rows:
                    self.ac_booking.insert(parent='', index='end', values=(row[0], row[1], row[2], row[3], row[4],row[5],row[6],row[7],row[8],row[9]))
        except Exception as err:
            print(f"Error: {err}")



if __name__ == "__main__":
    window = customtkinter.CTk()
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue") 
    window.after(0,lambda:window.state('zoomed'))
    user_dash = Dashboard(window)
    window.mainloop()
