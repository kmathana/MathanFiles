#!/usr/bin/env python
# coding: utf-8

# In[1]:


## filter, map, reduce
## it takes two arguments, funtion name, input to the function
## filter rerurns only true value


# In[20]:


## filter

def even(n):
    print("Function has started")
    if n%2 != 0:
        return True
    else:
        return False


# In[21]:


a = [1,2,3,4,5,6,7,8]
b = filter(even,a)
print((b))


# In[22]:


c = list(b)
print(c)


# In[23]:


print(c[0:2])


# In[25]:


a = [1,2,3,4,5,6,7,8]
print(list(filter(lambda x:x%2!=0,a)))


# In[27]:


## map
a = [1,2,3,4,5,6,7,8]
b = map(even,a)
print(list(b))


# In[28]:


a = [1,2,3,4,5,6,7,8]
print(list(map(lambda x:x%2!=0,a)))


# In[29]:


## reduce

from functools import reduce

numbers = [1, 2, 3, 4, 5]

def add(x, y):
    return x + y

sum_of_numbers = reduce(add, numbers)

print(sum_of_numbers)


# In[30]:


sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)


# In[ ]:


## ## filter, map, reduce


# In[32]:


squares_of_even_numbers = [x ** 2 for x in numbers if x % 2 == 0]
print(squares_of_even_numbers)


# In[34]:


add_numbers = [x for x in range(11)]
print(add_numbers)


# In[35]:


a = (1,2,3)
if bool(a):
    print("Value")
else:
    print("No")


# In[36]:


b = ()
if bool(b):
    print("Value")
else:
    print("No")


# In[37]:


a = ("test", "demo", "hello")
if "hi" not in a:
    print("yes")


# In[38]:


a = ("test", "demo", "hello")
if "test" in a:
    print("yes")


# In[39]:


##dict comprehension
a = ("test", "demo", "hello")
b = {1, 2, 3}
c = zip(a,b)
print(list(c))
 


# In[43]:


import random
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(random.choice(a))


# In[44]:


print(random.sample(a,5))


# In[49]:


random.shuffle(a)
print(a)


# In[50]:


print(random.randrange(0,500))


# In[51]:


print(random.uniform(1,5))


# In[52]:


import string
import random
print(string.ascii_letters)


# In[56]:


print(random.choice(string.ascii_letters))
print(random.randint(0,9))


# In[60]:


"".join(random.choice(string.ascii_letters) for i in range(10))


# In[61]:


print(string.punctuation)


# In[62]:


print(random.choice(string.punctuation))


# In[63]:


print(string.digits)


# In[66]:


"".join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(20))


# In[67]:


import math
print(math.ceil(22.09))
print(math.ceil(-22.09))
print(math.ceil(22))


# In[68]:


print(math.floor(22.09))
print(math.floor(-22.09))
print(math.floor(22))


# In[70]:


print(round(22.09))
print(round(-22.09))
print(round(22))


# In[71]:


file = open(r"C:\Users\k_mat\Python\Training\text_classifier_with_labels.csv","r")
for i in file:
    print(i)


# In[72]:


file.close()


# In[77]:


## Pandas
import pandas as pd
data = pd.read_csv(r"C:\Users\k_mat\Python\Training\text_classifier_with_labels.csv")


# In[79]:


data


# In[80]:


data.describe()


# In[81]:


data['text']


# In[82]:


data['label']


# In[ ]:




