class student:
    bal:int
    car:int

    def getdata(self):
        self.bal = int(input("Enter the balance: "))
        self.car = int(input("Enter the car value: "))
class var:
    bal:int
    car:int
    def getdata(self):
        self.bal =int(input("Enter the balance: "))
        self.car = int(input("Enter the car value: "))
class prime:
    bal:int
    car:int
    def getdata(self):
        self.bal = int(input("Enter the balance: "))
        self.car = int(input("Enter the car value: "))
class main(student, var, prime):
    def __init__(self):
        self.s=student()
        self.v=var()
        self.p=prime()

    def getdata(self):
        self.s.getdata()
        self.v.getdata()
        self.p.getdata()

    def printdata(self):
        print("Student Balance:", self.s.bal)
        print("Student Car:", self.s.car)
        print("Var Balance:", self.v.bal)
        print("Var Car:", self.v.car)
        print("Prime Balance:", self.p.bal)
        print("Prime Car:", self.p.car)
st= main()
st.getdata()
st.printdata()