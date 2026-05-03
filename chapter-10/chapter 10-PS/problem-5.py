# Write a class Train which has methods to book a ticket, get status (no of seats)and get fare information of train which has methods to book a ticket, get status of train running under Indian Railways.
from random import randint
class Train :
    def __init__(self,trainNo):
        self.trainNo = trainNo
    def book(self):
        print(f"Ticket is booked in train no:{self.trainNo}")
    def getStatus(self):
        print(f"Status of train no:{self.trainNo} is available")
    def getFare(self):
        print(f"Ticket fare in train no:{self.trainNo} is {randint(222,555)}")

        t = Train(12345)
        t.book()
        t.getStatus()
        t.getFare()
