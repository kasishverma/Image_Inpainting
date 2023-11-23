#!/usr/bin/env python
# coding: utf-8

# In[21]:


import os
path=os.chdir("C:\\Users\\DELL\\Documents\\Image Inpainting\\faulted\\k")
i=201
for file in os.listdir(path):
    new_file_name="Image_{}.jpg".format(i)
    os.rename(file, new_file_name)
    i=i+1


# In[ ]:




