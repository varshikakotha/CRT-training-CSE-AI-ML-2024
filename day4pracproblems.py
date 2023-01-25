#!/usr/bin/env python
# coding: utf-8

# In[3]:


n = int(input())
arr = []
for i in range(n):
    action = input().split()
    if action[0] == "add":
        arr.append(int(action[1]))
    elif action[0] == "insert":
        ele = int(action[1])
        ind = int(action[2])
        arr.insert(ind,ele)
    elif action[0] == "remove":
        ele = int(action[1])
        if ele in arr:
            arr.remove(ele)
    elif action[0] == "pop":
        if len(arr) > 0:
            arr.pop()
    elif action[0] == "print":
        if len(arr) != 0:
            print(*arr)
    else:
        print("Invalid Input")
        


# In[4]:


n = int(input())
for i in range(n):
    password = input()
    pass_len = len(password) >= 8 and len(password) <=16
    alp = password[0].isalpha()
    upper = False
    lower = False
    digit = False
    special = False
    for i in password:
        if i.isdigit():
            digit = True
        elif i.isupper():
            upper = True
        elif i.islower():
            lower = True
        else :
            special = True
    if pass_len and alp and upper and lower and digit and special == 1 :
        print("True")
    else:
        print("False")
            
    


# In[ ]:





# In[ ]:




