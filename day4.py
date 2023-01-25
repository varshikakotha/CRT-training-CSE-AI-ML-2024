#!/usr/bin/env python
# coding: utf-8
#packages
#code
from filename import functionname
variables = values // a = val,b = val,c = val...
print(function(arguments)) // arguments = a,b,c,...

import filename 
filename.(gives functions avali in that file)//used when functions in module are not known , modules or files are known as object
class student:
    #variables inside class are class variables for accesing them for class student object should be created and then values 
    #are accessed
    name = ""
    roll_number = ""
    branch = ""
    marks = 0
    attendence = 0.0
    is_using_transport = False
   # view_attendence()
   # view_marks()
   # view_name()
   # update_name(new_name)
    def view_attendence(self):
        # self is a keyword which says that the method is belongs to student class (this in java,c++)
        pass
    def view_marks(self):
        pass
    def view_name(self):
        pass
    def update_name(self,new_name):
        #self doesnot expect any argument
        pass
# In[1]:


#CONSTRUCTOR OR DESTRUCTOR
class Student:
    student_name = ""
    def __init__(self,name):
        print("object created")
        print(name)
a1 = Student("Varshika") #object is created and argument is passed into name in func
        


# In[2]:


#CONSTRUCTOR OR DESTRUCTOR
class Student:
    student_name = "no name" #want to access function within the class should be accessed through self keyword
    def __init__(self,name):
        print("object created")
        print(name)
        print(self.student_name)
a1 = Student("Varshika")
        


# In[5]:


#CONSTRUCTOR OR DESTRUCTOR
class Student:
    student_name = "no name"
    def __init__(self,name):
        self.student_name = name
        #print(name)
a1 = Student("Varshika") #a1,a2,a3 student object
a2 = Student("kumari") #want to access outside class use object name
a3 = Student("kotha")
print(a2.student_name)


# In[3]:


class Student:
    student_name = "no name"
    def __init__(self,name):
        self.student_name = name
    def update_name(self,new_name):
        self.student_name = new_name
s1 = Student("a")
s2 = Student("b")
s3 = Student("c")
print(s2.student_name)


# In[1]:


#to make private add two underscores before variables,private variables are accessible only within the class , 
#these are not accessible even with the objects created outside of the class


# In[3]:


class UserClass:
    full_name = ""
    email = ""
    __password=""
    mobile_number=""
    def __init__(self,name,email,password):
        self.full_name = name
        self.email = email
        
    def update_name(self,new_name):
        self.full_name = new_name
    def get_name(self): 
        return self.full_name
    """setter method for private variable password"""
    def update_password(self,new_password):
        self.__password = new_password
    def update_mobile_number(self,new_number):
        self.mobile_number = new_mobile_number
    def get_user_password(self):
        return self.__password


# In[4]:


from User import UserClass
class login:
    __db = []
    def __init__(self):
        self.print_menu()
    def print_menu(self):
        print("Welcome user")
        print("1.registration")
        print("2.login")
        print("3.exit")
    def create_user(self,name,email,password):
        new_user = UserClass(name,email,password) #obj for user
        self.__db.append(new_user)
        print(self.__db)
        return True
    def validate_user(self,email,password):
        temp = self.__db.copy()
        for user_obj in temp:
            if email == user_obj.email:
                if password == user_obj.get_user_password():
                    return "Login success"
                else:
                    return "password is incorrect"
            return "email is not found"   
obj = login()
while True:
    option = input("enter your choice")
    if option == 1:
        name = input("enter your full name:")
        email=("enter your email:")
        password = ("create new password:")
        res = obj.create_user(name,email,password)
        if res == True:
            print("user created succesfully")
        
    elif option == 2:
                
    elif option == 3:
        break
    else:
        print("Invalid Input")
obj.create_user("name","email","pass")
        


# In[ ]:


s = input()
if s[0] == 

