from models import *

# insert Student
name = input("Add name : ")
gender = input("Add gender : ")
email = input("Add email : ")
contact = input("Add contact : ")
address = (input("Add address : ")).split(",")
institute = input("Add institute : ")
reg = input("Add reg : ")
password = input("Add password : ")

# validate data
student = Students()
a = student.setName(name)
b = student.setGender(gender)
c = student.setEmail(email)
d = student.setContact(contact)
e = student.setAddress(address)
student.setInstitute(institute)
student.setReg(reg)
student.setPassword(password)

# complete database transaction
if a and b and c and d and e == True:
    print(student.set())
else:
    print("Invalid data, please correct")

# insert Authority

# insert Owner
