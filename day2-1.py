#!/usr/bin/env python
# coding: utf-8

# In[3]:


d={}
d.update({15:'varshika',
          11:'Bhargavi',
          13:'pravallika',
          17:'ramya',
          4:'janu'})


# In[4]:


d


# In[20]:


l = [1,2,3,4,6]
k = int(input())
flag = 0
for i in range(len(l)):
    if l[i] == k:
        print(i)
        flag = 1
        break
if flag == 0:
    print("element not found")


# In[21]:


#LIST COMPREHENSION
#l = [x for x in range(intial,final,stepsize1)]


# In[22]:


l=[x for x in range(2,11,2)]


# In[23]:


l


# In[31]:


# l =[num for num in range() condition]
l = [num for num in range(0,51) if num%2==0]
print(l)


# In[34]:


l = [num for num in range(1,101) if num%7==0 and num%11==0]
print(l)


# In[51]:


l = [6,5,4,3,2,1]
n = len(l)
print(n)
for i in range(n-1,-1,-1):
    if i == n-1:
        print("[")
    print(l[i],end = " ")
print("]")
    


# In[56]:


l = '1:2:3:4:5'.split(":")
l


# In[68]:


l = list(map(int,input().split()))
print(l)
p,n=0,0
for i in range(len(l)):
    if l[i]<0:
        n=n+l[i]
    elif l[i]>0:
        p=p+l[i]
print(p,n)

n = int(input())
i=1
while i<=n:
    l = list(map(int,input().split()))
   # print(i)
    i = i+1n=int(input())
l=[map(int,input().split()) for x in range(n)]
# In[ ]:


n = int(input())
arr = [map(int,input()).split() for i in range(n)]
i =0
j = i+1
for i in range(len(arr)):
    for j in range(len(arr)):
        print("i=",i)
        print("j=",j)
        if arr[i] == arr [j]:
            print(arr[i])


# In[ ]:




