from models import *

# # insert Student
# name = input("Add name : ")
# gender = input("Add gender : ")
# email = input("Add email : ")
# contact = input("Add contact : ")
# address = (input("Add address : ")).split(",")
# institute = input("Add institute : ")
# reg = input("Add reg : ")
# password = input("Add password : ")

# # validate data
# student = Students()
# a = student.setName(name)
# b = student.setGender(gender)
# c = student.setEmail(email)
# d = student.setContact(contact)
# e = student.setAddress(address)
# f = student.setInstitute(institute)
# g = student.setReg(reg)
# h = student.setPassword(password)

# # complete database transaction
# if a and b and c and d and e and f and g and h == True:
#     student.set()
# else:
#     print("Invalid data, please correct")

# insert Authority
# name = input('Add body name : ')
# email = input('Add email : ')
# contact = input('Add contact  : ')
# password = input('Add password : ')

# authority = Authorities()

# a = authority.setName(name)
# b = authority.setEmail(email)
# c = authority.setContact(contact)
# d = authority.setPassword(password)

# if a and b and c and d == True:
#     authority.set()
# else:
#     print("Invalid data, please correct")

# insert Owner
name = input('Add name : ')
gender = input('Add gender : ')
email = input('Add email : ')
contact = input('Add contact : ')
address = str(input('Add address : ')).split(',')
total = int(input('Add total : '))
verified = bool(input('Add verification status : '))
password = input('Add password : ')

owner = Owners()
a = owner.setName(name)
b = owner.setGender(gender)
c = owner.setEmail(email)
d = owner.setContact(contact)
e = owner.setAddress(address)
f = owner.setTotalProperties(total)
g = owner.setVerification(verified)
h = owner.setPassword(password)

if a and b and c and d and e and f and g and h == True:
    owner.set()
else:
    print('Invalid data, please correct')
