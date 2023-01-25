#!/usr/bin/env python
# coding: utf-8

# In[1]:


#SET
#union,intersection,difference


# In[2]:


s1 = {1,2,3}
s2 = {3,4,5,6}
res = s1.union(s2)
res1 = s1.intersection(s2)
res2 = s1.difference(s2)
print(res,res1,res2)


# In[3]:


#TUPLES
#index,count


# In[11]:


a,b,c,d = map(int,input().split())
#x, y = map(int, input().split ())
if a%2 == 0 or b%2 ==0 or c%2 ==0 or d%2 ==0:
    print("even")
else:
    print("odd")


# In[15]:


x = int(input())
print("even") if x%2==0 else print("odd")

if condition1:
    #code
elif condition2:
    #code
else:
    #code
# In[17]:


day = int(input())
if day ==1:
    print("sun")
elif day== 2:
    print("mon")
elif day ==3:
    print("tue")
elif day== 4:
    print("wed")
elif day== 5:
    print("thur")
elif day== 6:
    print("fri")
elif day ==7:
    print("sat")
else:
    print("number not found,enter in range 1 to 7")
    


# In[1]:


n = int(input())
if n>0 and n<20 :
    if n%2 ==0:
        print("weird")
    else:
        print("normal1")
elif n>=20 and n<30:
    print("normal2")
else :
    if n%2!=0:
        print("normal3")
    else:
        print("weird1")
    


# In[ ]:




