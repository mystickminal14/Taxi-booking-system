from tkinter import messagebox
import backend.storage as conn

class RegisterStorage:
    __connection__=None
    def __init__(self):
        self.__connection__=conn.Storage.Connect()

    def _CustomerRegistration(self,register):
        try:
            cursor=self.__connection__.cursor()
            insert_query= f"INSERT INTO `customer_registration`(`customer_id`, `firstName`, `lastName`, `age`, `gender`, `dateOfBirth`, `phone`, `country`, `email`, `password`) VALUES ('{register.getId()}','{register.getFirstName()}','{register.getLastName()}','{register.getAge()})','{register.getGender()}','{register.getDOB()}','{register.getPhoneNumber()}','{register.getCountry()}','{register.getEmailAddress()}','{register.getPassword()}')"
            cursor.execute(insert_query)
            self.__connection__.commit()
            cursor.close()
            return True
        except Exception as e:
            print(e)
            return False
    def _DriverRegistration(self,register):
        try:
            cursor=self.__connection__.cursor()
            insert_query= f"INSERT INTO `driver_registration`(`driver_id`, `fname`, `lname`, `age`, `gender`, `dateofBirth`, `country`, `pno`, `email`, `passcode`, `license`, `experience`)  VALUES ('{register.getId()}','{register.getFirstName()}','{register.getLastName()}','{register.getAge()})','{register.getGender()}','{register.getDOB()}','{register.getPhoneNumber()}','{register.getCountry()}','{register.getEmailAddress()}','{register.getPassword()}','{register.getLicense()}','{register.getExperience()}')"
            cursor.execute(insert_query)
            self.__connection__.commit()
            cursor.close()
            return True
        except Exception as e:
            print(e)
            return False
    
    def CustomerLogin(self,CustomerLogin):
        try:
            cursor = self.__connection__.cursor()
            cursor.execute("SELECT * FROM customer_registration WHERE email='"+CustomerLogin.getUsername()+"' AND password='"+CustomerLogin.getPassword()+"'")
            record = cursor.fetchone()
        except Exception as e:
            print(e)
        return record
    def ManagerLogin(self,ManagerLogin):
        try:
            cursor = self.__connection__.cursor()
            cursor.execute("SELECT * FROM manager WHERE username='"+ManagerLogin.getUsername()+"' AND passcode='"+ManagerLogin.getPassword()+"'")
            record = cursor.fetchone()
        except Exception as e:
            print(e)
        return record
    def DriverLogin(self,DriverLogin):
        try:
            cursor = self.__connection__.cursor()
            cursor.execute("SELECT * from driver_registration WHERE email='"+DriverLogin.getUsername()+"' AND passcode='"+DriverLogin.getPassword()+"' AND status='active'")
            dummy = cursor.fetchone()
        except Exception as e:
            print(e)
        return dummy
    
    def ReserveRide(self,BookRide):
        try:
            cursor=self.__connection__.cursor()
            book_query= f"INSERT INTO `reservation`(`book_id`, `location`, `destination`, `time`, `date`,`customer_id`) VALUES ('{BookRide.getId()}','{BookRide.getLocation()}','{BookRide.getDestination()}','{BookRide.getTime()})','{BookRide.getDate()}','{BookRide.getCustomerId()}')"
            cursor.execute(book_query)
            self.__connection__.commit()
            cursor.close()
            return True
        except Exception as e:
            print(e)
            return False
    