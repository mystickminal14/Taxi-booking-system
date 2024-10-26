class CustomerRegistration:
    def __init__(self,_customer_id=None,_first_name=None,_last_name=None,_age=None,_gender=None,_date_of_birth=None,_country=None,_number=None,_email=None,_password=None):
        self.customer_id=_customer_id
        self.first_name=_first_name
        self.last_name=_last_name
        self.age=_age
        self.gender=_gender
        self.date_of_birth=_date_of_birth
        self.country=_country
        self.number=_number
        self.email=_email
        self.password=_password

    def getId(self):
        return self.customer_id
    
    def setId(self,cust_id):
        self.customer_id=cust_id

    def getFirstName(self):
        return self.first_name
    
    def setFirstName(self,first_name):
        self.first_name=first_name
    
    def getLastName(self):
        return self.first_name
    
    def setLastName(self,last_name):
        self.last_name=last_name

    def getAge(self):
        return self.age
    
    def setAge(self,age):
        self.age=age
    
    
    def getGender(self):
        return self.gender
    
    def setGender(self,gender):
        self.gender=gender
    
    def getDOB(self):
        return self.date_of_birth
    
    def setDOB(self,date_of_birth):
        self.date_of_birth=date_of_birth
        
    def getCountry(self):
        return self.country
    
    def setCountry(self,country):
        self.country=country
    
        
    def getPhoneNumber(self):
        return self.number
    
    def setPhoneNumber(self,number):
        self.number=number

        
        
    def getEmailAddress(self):
        return self.email
    
    def setEmailAddress(self,email):
        self.email=email
    
    def getPassword(self):
        return self.password
    
    def setPassword(self,password):
        self.password=password