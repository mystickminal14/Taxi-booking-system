class BookRide:
    def __init__(self,book_id=None,_location=None,_destination=None,_time=None,_date=None,_cusId=None):
        self.book_id=book_id
        self.location=_location
        self.destination=_destination
        self.time=_time
        self.date=_date
        self.cusId=_cusId
      


    def getId(self):
        return self.book_id
    
    def setId(self,book_id):
        self.book_id=book_id
    def getLocation(self):
        return self.location
    
    def setLocation(self,location):
        self.location=location
    
    def getDestination(self):
        return self.destination
    
    def setDestination(self,destination):
        self.destination=destination

    def getTime(self):
        return self.time
    
    def setTime(self,time):
        self.time=time
    
    
    def getDate(self):
        return self.date
    
    def setDate(self,date):
        self.date=date
    
    def getCustomerId(self):
        return self.cusId
    
    def setCustomerId(self,cusId):
        self.cusId=cusId
    
    
   