
# coding: utf-8

# In[ ]:

from selenium import webdriver  # powers the browser interaction
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()


# In[7]:

driver.get("https://www.playshakespeare.com/library")


# In[25]:

root = "https://www.playshakespeare.com"


# In[26]:

urls = [(x.text.strip(), root + x['href']) for x in soup.select('div.docman_categories')[0].select("a") if "Folder" not in x.text.strip()]


# In[ ]:

for u in urls_dl:
    driver.get(u)
    soup = BeautifulSoup(driver.page_source, "lxml")
    for a in soup.select("a"):
        try:
            link = a['href']
            if "v3" in link and "xml" in link and "file" in link:
                download = root + link
        except:
            pass
        
    driver.get(download)
    
    time.sleep(3)


# In[42]:




# In[ ]:



