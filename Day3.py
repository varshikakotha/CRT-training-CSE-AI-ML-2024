#!/usr/bin/env python
# coding: utf-8

# In[2]:


d = {
    'key1' : 'value1'
}
d.update({'name':'user name'})
d.update({'branch':'CSE'})
d.update({'section':'A'})
for i in d:
    print('key:',i)
    print("value:",d[i])


# In[5]:


l=[]
p=int(input("p="))
for i in range (p):
    n=int(input("n="))
    s = {}
    for i in range (n):
      k=input("enter k:")
      value=input("enter val:")
      s.update({k: value})
    l.append(s)
print(l)


# In[8]:


l = []
d = {}
for i in range(2):
    d.update({
       "key1":input("enter val1:"),
       "key2":input("enter val2:")
    })
    l.append(d)
print(l)


# In[10]:


a = [1,2,3]
b = a
b[0] = 10
print(a)
print(b)


# In[25]:


l=[]
p=int(input("p="))
for i in range (p):
    n=int(input("n="))
    s = {}
    for i in range (n):
      k=input("enter k:")                           
      value=input("enter val:")
      s.update({k: value})
    l.append(s)
print(l)
user = input()
pw = input()
for i in range(len(l)):
    if user == d[i].keys() and pw == d[i].values():
        print("yes")
    else:
        print("no")


# In[15]:


db = [
    {'abc':'123'},{"def":"456"},{"ghi":"789"},{"jkl":"147"}
]
#user = input()
#pw = input()
for i in range(len(db)):
    print(db[i])
    for u in db[i]:
        print(u)
    
    


# In[23]:


db = [
    {'abc':'123'},{"def":"456"},{"ghi":"789"},{"jkl":"147"}
]
#print(db)
user = input("enter username:")
pw = input("enter pw:")
#for i in db:
    #print(i.keys())
    #print(i.values())
    #print(i.items())
temp = {user:pw}
if temp in db:
     print("correct")
else:
    print("incrct")


# In[28]:


#ARRAYS
row = 3
col = 3
arr = []
for i in range(row):
    element=[]
    for j in range(col):
        element.append((int(input("Enter element:"))))
    arr.append(element)
print(arr)


# In[29]:


row = 3
col = 3
arr = []
arr1 = []
for i in range(row):
    element=[]
    for j in range(col):
        element.append((int(input("Enter element:"))))
    arr.append(element)
print(arr)
for i in range(row):
    element=[]
    for j in range(col):
        element.append((int(input("Enter element:"))))
    arr1.append(element)
print(arr1)


# In[34]:


row =2
col=2
arr1 =[]
for i in range(row):
    temp = input("enter elements in row:").split()
    ele = list(map(int,temp))
    arr1.append(ele)
print(arr1)
arr2 = []
for i in range(row):
    temp = input("enter elements in row:").split() #b = list(map(int,input("enter ele").split(" ")))
    ele = list(map(int,temp))                      #new_arr.append((b))
    arr2.append(ele)
print(arr2)
res = [[0 for j in range(col)] for i in range(row)]
for i in range(row):
    for j in range(col):
        res[i][j] = arr1[i][j]+arr2[i][j]
print(res)


# In[4]:


#SLICING
l = [1,2,3,4,5,6,7,8,9,10]
print(l)
print(l[0:5])#index starts at 0 and last value is not included and initial value is included
print(l[0:10:2])


# In[5]:


l = [1,2,3,4,5,6,7,8,9,10]
print(l[::2])#all the three arguments are optial[start,end,stepsize]


# In[6]:


print(l[::-1])


# In[9]:


#negative indexing starts from -1 ,-1 prints last element of list
print(l[-9])


# In[12]:


i=0
j =1
count =0
while count<25:
    val = i+j
    l.append(val)
    i = j
    j = val
    count = count+1
print(l)


# In[ ]:


#STRING METHODS
#1.captilize
#2.split,join
#3.title
#4.lower,upper
#5.count
#6.swapcase
#7.isalpha,isalnum


# In[1]:


#floatingpoint numbers -- {:.6f}
#try and except


# In[ ]:


#calculator builing


# In[7]:


try:
    for i in range(5):
        n = int(input())#arr = list(map(int,input()).split())
except:
    print("enter integer value")
        


# In[31]:


#FUNCTIONS
#regular functions
#default value functions
#keyword argument functions
#variable length


# In[13]:


def prime(num):
    c=1
    count =0
    while c<=num:
        if num%c == 0:
            count = count+1
        c = c+1
    if count == 2:
        print("prime")
    else:
        print("not prime")
p = int(input("enter number:"))
prime(p)


# In[20]:


def prime(num):
    count = 0
    it =0
    for i in range(1,num+1):
        if num%i == 0:
            count = count+1
        it = it+1
    print(it)
    if count == 2:
        print("prime")
    else:
        print("not prime")
n = int(input())
prime(n)


# In[22]:


def prime(num):
    count = 0
    it =0
    for i in range(2,num):#exculding 1 and num itself
        if num%i == 0:
            count = count+1
        it = it +1
    print(it)
    if count == 0:
        print("prime")
    else:
        print("not prime")
n = int(input())
prime(n)


# In[26]:


def prime(num):
    count = 0
    it =0
    for i in range(2,num//2):
        if num%i == 0:
            count = count+1
        it = it+1
    print(it)
    if count == 0:
        print("prime")
    else:
        print("not prime")
n = int(input())
prime(n)


# In[29]:


num = int(input())
count =0
for i in range(2,int(num**0.5)+1):
    if num%i == 0:
        count +=1
print(i)
if count == 0:
    print("prime")
else:
    print("not")
    


# In[32]:


#defalut value functions 
#if any argument is not given default value given while defining function will be taken


# In[35]:


#keyword argument 
#by defining keyword in arguments order can be in any order
def num(a,b,c,d):
    print(a,b,c,d)
num(10,c = 30,d=40,b=20)
    


# In[37]:


#variable length
def add(*abc):
    print(abc)
add(10,20,'hello',[1,23])


# In[42]:


def add (*abc):
    sum(abc)
    print(sum(abc))
add(1,2,3)


# In[44]:


def add(*abc,a,b,c,d):
    res1 =1
    for i in abc:
        res1 += i
    return res1
print(add(1,2,3,4))


# In[45]:


def add(a,b,*abc):
    res1 =1
    for i in abc:
        res1 += i
print(add(1,2,3,4))


# In[46]:


def check(n):
    print(n)
    if n>0:
        check(n-1)
check(5)


# In[10]:


n = int(input())
d = {}
for i in range(n):
    print(i)
    roll,name = input().split(",")
    d.update({roll,name}) #wrong
print(d)


# In[15]:


n=int(input("n="))
s = {}
for i in range (n):
    k=input("enter k:")
    value=input("enter val:")
    s.update({k: value})
print(s)                     #wrong
val = input()
for i in d.keys():
    #print(p)
    #print(k)
    if val == i:
        print(k)


# In[17]:


l=[]
p=int(input("p="))
for i in range (p):
    #n=int(input("n="))
    s = {}
    #for i in range (n):
    k=input("enter k:")                           
    value=input("enter val:")
    s.update({k: value})
    l.append(s)
print(l)
user = input()
pw = input()
for i in range(len(l)):
    if user == l[i].keys() and pw == l[i].values():
        print("yes")
    else:
        print("no")


# In[30]:


l=[]
p=int(input("p="))
for i in range (p):
    #n=int(input("n="))
    s = {}
    #for i in range (n):
    k,value=input().split(",")
    #value=input("enter val:")
    k = int(k)
    s.update({k: value})
    l.append(s)
print(l)
val = int(input())
for i in range(len(l)):
    #print(val)
    #print(l[i].keys())
    #print(l[i].values())
    if l[i].keys() == val:
        print(l[i].values())   #wrong


# In[33]:


n = int(input())
arr = [(int,input().split()) for x in range(n)]
print(arr)


# In[ ]:




