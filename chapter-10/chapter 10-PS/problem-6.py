#Can you change the self-parameter inside a class to something else(say saqnvi)Try changing self self to slf or sanvi and see the effects

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

        #If we change the self parameter to something else, it will not work because self is a convention in Python and it is used to refer to the current object. If we change it to something else, it will not be recognized as a reference to the current object and we will get an error. For example, if we change self to sanvi, we will get an error because sanvi is not defined as a reference to the current object.
