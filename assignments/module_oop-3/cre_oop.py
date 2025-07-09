class student:
    stid=12
    stnm= "Ravi"
    stmarks= 90
    

    def getdata(self):
        print("Student ID:", student.stid)
        print("Student Name:", student.stnm)
        print("Student Marks:", student.stmarks)

st=student()
print("Student ID:", st.stid)
print("Student Name:", st.stnm)
st.getdata()
print("Student Marks:", st.stmarks)