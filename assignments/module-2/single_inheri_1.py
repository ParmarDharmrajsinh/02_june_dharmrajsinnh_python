class father:
    bal:int
    car:int

    def getdata(self):
        self.bal = int(input("Enter the balance: "))
        self.car = int(input("Enter the car value: "))
    
class son(father):
    def printdata(self):
        print("Balance:", self.bal)
        print("car:",self.car)
sn= son()
sn.getdata()
sn.printdata()
