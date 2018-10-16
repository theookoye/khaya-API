from imports import db
from validate_email import validate_email

# helper functions


def insertStudent(a, b, c, d, e, f, g, h):
    task = False

    try:
        db.Students.insert_one({'Name': a, 'Gender': b, 'Email': c, 'Contact': d,
                                'Permanent Address': e, 'Institute': f, 'Reg': g, 'Password': h})
        task = True
        return task
    except Exception:
        return task


def insertOwner(a, b, c, d, e, f, g, h):
    task = False

    try:
        db.Owners.insert_one({'Name': a, 'Gender': b, 'Email': c, 'Contact': d,
                              'Permanent Address': e, 'Total Properties': f, 'Password': g, 'Verified': h})
        task = True
        return task
    except Exception:
        return task


def insertAuthority(a, b, c, d):
    task = False

    try:
        db.Owners.insert_one({'Name': a, 'Email': b, 'Contact': c,
                              'Password': d})
        task = True
        return task
    except Exception:
        return task


def insertProperty(a, b, c, d, e, f, g, h, i, j):

    task = False

    try:
        db.Properties.insert_one({'Owner ID':a, 'Address':b, 'Facilities':c, 'Shared':d, 'Verified':e, 'Capacity':f, 'Media':g, 'Room':h, 'Description':i, 'Likes':j})
        return task

    except Exception:
        return task


def insertReview(a, b, c, d):
    
    task = False

    try:
        reviews = []
        query = db.Properties.find_one({'Property ID':a}, {'Reviews':'1'})

        for i in query:
            reviews.append(i['Review'])
        
        reviews.append(b,c,d)

        db.Properties.update_one({'Property ID':a}, {'$set':{'Reviews':reviews}})

        task = True
        return task
    except Exception:
        return task


class Students(object):
    # private instance variables
    __name, __gender, __email, __contact, __institute, __reg, __address, __password = (
        "", "", "", "", "", "", "", "")

    def setName(self, name):
        if type(name) == str and str(name).isdigit == False and len(name) > 0:
            self.__name = name
            return True
        else:
            return False

    def setGender(self, gender):
        if gender == 'Male' or gender == 'Female':
           self.__gender = gender
           return True
        else:
            return False

    def setEmail(self, email):
        if validate_email(email) == True:
            self.__email = email
            return True
        else:
            return False

    def setContact(self, contact):
        if type(contact) == str:
            self.__contact = str(contact).strip()
            return True
        else:
            return False

    def setInstitute(self, institute):
        self.__institute = institute

    def setReg(self, reg):
        self.__reg = reg

    def setAddress(self, address):
        if type(address) == list and len(address)==4:
            self.__address = address.copy()
            return True
        else:
            return False

    def setPassword(self, password):
        self.__password = password

    def set(self):
        insertStudent(self.__name, self.__gender, self.__email, self.__contact,
                  self.__institute, self.__reg, self.__address, self.__password)


class Owners(object):
    # private instance variables
    __name, __gender, __email, __contact, __address, __totalProperties, __password, __verified = (
        "", "", "", "", "", "", "", "")

    def setName(self, name):
        if type(name) == str and str(name).isdigit == False and len(name) > 0:
            self.__name = name
            return True
        else:
            return False

    def setGender(self, gender):
        if gender == 'Male' or gender == 'Female' or gender == 'Corporate':
           self.__gender = gender
           return True
        else:
            return False

    def setEmail(self, email):
        if validate_email(email) == True:
            self.__email = email
            return True
        else:
            return False

    def setContact(self, contact):
        self.__contact = contact

    def setAddress(self, address):
        if type(address) == list and len(address)==4:
            self.__address = address.copy()
            return True
        else:
            return False

    def setTotalProperties(self, total):
        if type(total) == int and total > 0:
            self.__totalProperties = total
            return True
        else:
            return False

    def setPassword(self, password):
        self.__password = password

    def setVerification(self, verified):
        self.__verified = False

    def set(self):
        insertOwner(self.__name, self.__gender, self.__email, self.__contact, self.__address,
                self.__totalProperties, self.__password, self.__verified)


class Authorities(object):

    # private instance variables
    __name, __email, __contact, __password = (
        "", "", "", "")

    def setName(self, name):
        if type(name) == str and len(name) > 0:
            self.__name = name
            return True
        else:
            return False

    def setEmail(self, email):
        if validate_email(email) == True:
            self.__email = email
            return True
        else:
            return False

    def setContact(self, contact):
        self.__contact = contact

    def setPassword(self, password):
        self.__password = password

    def set(self):
        insertAuthority(self.__name,  self.__email, self.__contact, self.__password)


class Properties(object):

    # private instance variables
    __ownerID, __address, __facilities, __shared, __verified, __capacity, __media, __room, __description, __likes = ("","","","","","","","","", "")

    def setOwnerID(self, ownerID):
        self.__ownerID = ownerID

    def setAddress(self, address):
        if type(address) == list and len(address)==4:
            self.__address = address.copy()
            return True
        else:
            return False

    def setFacilities(self, facilities):
        if type(facilities) == list and len(facilities) > 0:
            self.__facilities = facilities.copy()
            return True
        else:
            return False

    def setShared(self, shared):
        if type(shared) == bool:
            self.__shared = shared
            return True
        else:
            return False

    def setVerification(self, verified):
        self.__verified = False

    def setCapacity(self, capacity):
        self.__capacity = capacity

    def setMedia(self, media):
        self.__media = media

    def setRoom(self, room):
        self.__room = room
    
    def setDescription(self, description):
        self.__description = description

    def setLikes(self):
        self.__likes = 0

    def set(self):
        insertProperty(self.__ownerID, self.__address,  self.__facilities, self.__shared,  self.__verified,  self.__capacity, self.__media,  self.__room,  self.__description, self.__likes)

class Reviews(object):

    # private instance variables
    __propertyID, __message, __anonymous, __author = ("","","","")

    def setPropertyID(self, propertyID):
        self.__propertyID = propertyID

    def setMessage(self, message):
        self.__message = message

    def setAnonymous(self, anonymous):
        if type(anonymous) == bool:
            self.__anonymous = anonymous
            return True
        else:
            return False

    def setAuthor(self, author):
        self.__author = author

    def set(self):
        insertReview(self.__propertyID, self.__message, self.__anonymous, self.__author)