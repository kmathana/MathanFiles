#!/usr/bin/env python
# coding: utf-8

# ## Class 5 - 25th Feb 2023

# In[50]:


a = 10
b = 20


# In[3]:


def add(a,b):
    print(a+b)


# In[4]:


add(1000,5)


# In[5]:


# def --> define a function
## add --> function name
## a,b --> argument name


# In[6]:


## local variable
## global variable


# In[12]:


def add(a,b):
    c = a+b
    print("Start of Function")
    return (a+b)
    print("after return")
c = add(5,4)


# In[13]:


add(10,5)


# In[14]:


add(c,10)


# In[15]:


add (c,20)


# In[16]:


add(c,20)


# In[18]:


a = "welcome" #global
def test():
    a  = "hello" # local
    return a
print(a)
a = test()
print(a)


# In[19]:


print(a)


# In[21]:


a = "welcome" #global
def test():
    global a
    a  = "hello" # local
    print (a)


# In[24]:


print(a)
test()


# In[25]:


a = "welcome" #global
def test():
    global a
    a  = "now changed" # local
    print (a)


# In[26]:


test()


# In[28]:


def name (f_name, m_name, l_name):
    print("First Name is: ", f_name)
    print("Middle Name is: ", m_name)
    print("Last Name is: ", l_name)


# In[29]:


name ("Sachin", "Ramesh", "Tendulkar") #positional Argument


# In[30]:


name (m_name = "Ramesh", f_name = "Sachin", l_name = "Tendulkar") #keyword Argument


# In[31]:


def name (f_name, m_name = None, l_name):
    print("First Name is: ", f_name)
    print("Middle Name is: ", m_name)
    print("Last Name is: ", l_name)


# In[32]:


def name (f_name, m_name, l_name = None):
    print("First Name is: ", f_name)
    print("Middle Name is: ", m_name)
    print("Last Name is: ", l_name)


# In[33]:


name("Sachin", "Tendulkar")


# In[36]:


def test (*args):
    print(args)
    print(a,b)


# In[37]:


test("hello","1","world")


# In[38]:


def test(**kwargs):
    print(kwargs)
    name = kwargs.get("name")
    state = kwargs.get("state")
    print(name, state)
    return name, state


# In[39]:


test(name = "user1", add1 = "add", add2 = "just some", state = "My State")


# In[40]:


def mul(a, b, c=1):
    print(a*b*c)
mul(3,4)


# In[41]:


mul(3,3,3)


# In[42]:


## lamda #in line


# In[43]:


def add(a,b):
    return a+b
c = add(5,4)
print(c)


# In[45]:


a = lambda a,b : a+b
a(5,4)


# In[49]:


a = lambda *args : args
a(1,2,3,4)

