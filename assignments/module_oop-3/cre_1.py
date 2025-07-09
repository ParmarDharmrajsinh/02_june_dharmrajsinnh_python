class student:
    stid=int(input("Enter Student ID: "))
    stname=input("Enter Student Name: ")


    def getdata(self):
        print("Student ID:", student.stid)
        print("Student Name:", student.stname)
st = student()
st.getdata()
