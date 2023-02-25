#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = [["kiran","20","Chennai"],["Madurai","Kumar","45"]]


# In[2]:


print(isinstance(a,list))


# In[3]:


a = {"Name" : "Mathankumar", "Nationality" : "India" , "Age" : 34}


# In[4]:


print(a.get("Name"))
print(a.get("Age"))
print(a.get("Nationality"))


# In[5]:


print(a.keys())


# In[6]:


print(a.values())


# In[7]:


print(a.items())


# In[8]:


a["Salary"] = 300
print(a)


# In[9]:


b = a.popitem()
print(a)
print(b)


# In[13]:


c = [1, 2, 3]
e = ["Name", "Age", "Nationality"]
d = dict(zip(a,c))
print(d)


# # Data types:  string(), int(), list(), tuple(), set(), dict() - Completed

# # Arithmatic operators

# In[20]:


a = 10
b = 9
print("+") 
print(a+b)
print("-") 
print(a-b)
print("x") 
print(a*b)
print("^") 
print(a^b) ## exponential or a**b
print(a/b)
print(a%b) ## Remainder
print(a//b)


# In[22]:


## relationale operators
print (a==b)
print(a!=b)
print(a>b)
print(a>=b)
print(a<b)


# In[23]:


## Logical Operator
## and , ## or, ## not
print (True and True)


# In[24]:


print(True and False)


# In[25]:


print(True or False)


# In[26]:


print(not True)


# In[27]:


print (not False)


# In[28]:


### loops


# In[29]:


## if
## while
## for


# In[30]:


## if loop -> decision making statement


# In[39]:


name = "kiran"
mark = 50

if name == 'kiran' and mark == "50":
    print('yes')
else:
    print('No')
print("********************************")

name = "kiran"
mark = 90

if name == 'kiran' and mark == "50":
    print('yes')
else:
    print('No')


# In[40]:


## nested if
if name == "kiran" and mark > 35:
    if mark > 60:
        print("First Class")
    else:
        print("Second Class")
else: 
    print("Fail")


# In[41]:


## if and elif

if mark ==100:
    print("centum")
elif mark >=90:
    print("A Grade")
elif mark >=60:
    print("1st Class")
elif mark >=40:
    print("3rd Class")
else:
    print("Fail")


# In[42]:


#while loop


# In[ ]:





# In[1]:


a = 1

while a<4:
    print(a)
    a = a + 1


# In[2]:


## for


# In[22]:


list(range(10, 25))


# In[4]:


list(range(10, 50, 10))


# In[33]:


for i in range(100, 1500, 500):
    print(i)


# In[48]:


a = "Hello world, today we are learning python"
a = a.split(" ")
print(a)
for i in a:
    if i == "python":
        print("Python is there")


# In[62]:


a = "Hello world, today we are learning python"
print(a)


# In[63]:


a = a.split(" ")
print(a)


# In[64]:


for i in a:
    print(i)


# In[65]:


a = {"Name" : "Mathankumar", "Nationality" : "India" , "Age" : 34}


# In[66]:


a.keys()


# In[67]:


for i in a.keys():
    print(i)


# In[68]:


for i in a.values():
    print(i)


# In[69]:


for i in a.items():
    print(i)


# In[79]:


for key, value in a.items():
    print(key)
    print(value)


# In[82]:


list(range(10,20,2))


# In[87]:


l = []
for i in range(10, 20):
    if i % 2 == 0:
        l.append(i)
print(l)


# In[110]:


a = ["apple", "apple", "mango", "mango", "orange"]
# Fruit : Count
#2 Unique Fruit List
#3 Duplicate Fruit List
print("#1 - Answer")
Counter(a)
print(fruit.count())
print("************************")
print("#2 - Answer")
print(set(a))


# In[ ]:




