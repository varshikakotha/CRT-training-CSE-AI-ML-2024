#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = '''a
b
c'''
type(a)


# In[2]:


a


# In[3]:


i = 9
a = 10.0
b = "string"
c = 'another string'
d = '''used
       in 
       documentation'''
flag =True,False
com = 10j
lst = [1,2,'a','string',[2,2j]] #once defined can change
d


# In[4]:


tup = (1,2,3) #once defined cannot be changed 
tup


# In[6]:


tup [0]
#tup[0] = 0


# In[7]:


tup1 = (1)


# In[8]:


type(tup1)


# In[9]:


tup2 = (1,)
type(tup2)


# In[10]:


lst1=[1]
type(lst1)


# In[11]:


#due to parenthesis used in BODMAS rule and given value to them,
#single element in parentesis is considered as int value if coma(,) is given then it is considered as tuple


# In[12]:


s = {1,2,3,4,1,5,6,8,5,3,3,3,3} 
# doesn't allow duplicate elements,allows all datatypes,doesnot follow indexing (insertion order is not necessary,follows random order)
type(s)


# In[15]:


s


# In[16]:


print(type(s))


# In[17]:


s1={[1,2,3],[4,5,6]} #  lists cannot be taken in set


# In[18]:


s2 = {[1,2,3],1,2,3}


# In[19]:


s3={[1,2,3]}


# In[20]:


s4 = {(1,2,3)}


# In[22]:


print(s4)
type(s4)


# In[23]:


#ARTHIMETIC OPERATOR
a = 1+2
b = 10-9
c = 10*10
d1 = 5/2 #float division
d2 = 5//2 # int division or floor division
print(d1,d2)


# In[24]:


sum_of_numbers = 1+2 
MulOfNumbers = 1*2
# two types of naming conventions


# In[25]:


r = 10%2 #reminder
print(r)


# In[28]:


# LOGICAL OPERATIONS (and ,or,not)
print(0 and 0)
print(0 and 1)
print(1 and 1)
print(1 and 0)

print(0 or 0)
print(0 or 1)
print(1 or 1)
print(1 or 0)


# In[ ]:


#BINARY REPRESENTATION
# 23 = 0001 0111 (can be represented using 4 bits or 8 bits) 


# In[29]:


print(23 and 7)


# In[30]:


#compiler does this by converting value into binary value and calculates by every BIT
#bin() function converts int values to binary values(binary string)
#23 = 10111 AND
#7 =  00111
#returns (00111)=7 THIS ALL PROCESS IS DONE IN BITWISE BINARY OPERATORS


# In[31]:


print(31 and 74)
print(74 and 31)


# In[32]:


print(bin(74))
print(type(bin(74)))


# In[34]:


bin(74)
bin(31)


# In[35]:


bin(31)


# In[36]:


bin(74)


# In[37]:


print(74 or 31)
print(31 or 74)


# In[41]:


print(74 and -31)
print(-74 and 31)


# In[38]:


# COMPARISION OR RELATIONAL OPERATOR
#>,<,>=,<=,==,!= ( output is true or false)


# In[40]:


print(31<74)
type(31<74)


# In[43]:


#ASSIGNMENT OPERATORS
#=,+=,-=,*=,/=,%=


# In[44]:


#BITWISE OPERATORS
#|,&


# In[46]:


#MEMBERSHIP OPERATOR
# in ,not in
l = [1,2,3,4,5,6,7]
print(5 in l)
print(5 not in l)


# In[47]:


#IDENTITY OPERATOR
# is
a = 10
b = None
print(a is 1)
print(b is None)


# In[49]:


#(condition)?True part : False part (other programming languages)
# True part if condition else False part (python)


# In[50]:


#list methods
#append-- l.append() -- append takes only one value
#len () function finds len of list
#pop() if index value is specified it is poped or last value will be poped
#remove() if value is not given returns error
#insert(index,value) return none
#list1.extend(list2) all contents of list2 goes into list1(combining two lists),to add any value to list it should be converted to list
#count(value) returns count in list,frequency of a element in list
#list.copy() no arguments are taken
#a.sort() default is ascending does not return anything to get in descending order [a.sort(reverse = True)]
#a.reverse() gives values of list in reverse order
#a.sorted()
#clear() removes elements from the list but list is not deleted


# In[51]:


#DIFFERENCE BETWEEN POP AND REMOVE
#1. in POP index value is considered , in REMOVE done by value 
#2. in POP value will be returned , in REMOVE value is not returned default val is null
#3. in POP index value is not mandatory ,in REMOVE value must be given


# In[53]:


lt = []
lt.append(1)
lt.append(1.9)
lt.append((1,2,3))
lt.append([1,2,3,4])
lt.append('string')


# In[54]:


lt


# In[56]:


len(lt)


# In[60]:


lt.pop(0)
print(lt)


# In[61]:


lt.pop()
lt


# In[62]:


lt1 = [1,2,3,4,5]
lt1.remove(2)
lt1


# In[63]:


lt1.insert(1,2)


# In[64]:


lt1


# In[65]:


lt1.count(2)


# In[68]:


lt2 = []
lt2 = lt1.copy()
lt2


# In[70]:


x = [10,20,30]
y = x
print(y)
y[0] = 100
print(x)
print(y)


# In[72]:


# to avoid prob in out 70 copy is used 
x = [10,20,30]
y = x.copy()
y[0] = 100
print(x)
print(y)


# In[73]:


w = [3,1,2]
z = sorted(w)
print("z=",z)
print("w=",w)


# In[78]:


w = [3,1,2]
z = sorted(w,reverse = True)
print("z=",z)
print("w=",w)


# In[79]:


a = int('1')
b = 2
print(a+b)


# In[85]:


a =  'bhagi is '
b = str(100)
c =' years old'
res = a+c
res1 = a+b+c
print(res)
print(res1)


# In[83]:


a = list('12345')
print(a)


# In[86]:


b = map(int,a)
print(b) 


# In[88]:


#value is stored at map address ,to convert map value address to list
a= list('67890')
b = list(map(int, a))
print(b)


# In[89]:


a= list('67890')
b = list(map(float, a))
print(b)


# In[ ]:


#TYPE CONVERSION
#implicit - complier do itself
#explicit -  user need to type cast

