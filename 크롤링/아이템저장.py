#!/usr/bin/env python
# coding: utf-8

# In[36]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


from time import sleep

import pandas as pd


# In[37]:


ns_address = "https://www.dualsonic.com/board/power_review.html#listPowerReview"


# In[38]:


header = {'User-Agent': ''}
#d = webdriver.Chrome('C:\\Users\\hyejin\\AppData\\Local\\Temp\\_AZTMP0_\\chromedriver.exe') # webdriver = chrome
d = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
d.implicitly_wait(3)
d.get(ns_address)

sleep(2)


# In[39]:


path_index = []
for i in range(1,11):
    path_string = '/html/body/div[3]/div[3]/div/div/div[1]/div[2]/ul/li['+ str(i) + ']/table/tbody/tr/td[2]/' 
    path_index.append(path_string)
    
print(path_index)


# In[40]:


#데이터 프레임 생성
review_df = pd.DataFrame(columns=['item','date', 'star',  'startext', 'review'])


# In[41]:


page_loop = 0
df_cnt = 0


while True :

    for index in path_index:
    
        try:
            xpath_item = index +  'div[1]/div[1]/span[1]'
            xpath_date = index + 'ul[1]/li[2]'
            xpath_star = index + 'div[1]/div[2]/span[1]/em'
        
            xpath_star_text = index + 'div[1]/div[2]/span[2]'
            xpath_review = index + 'div[1]/div[3]/p'
            xpath_review_more = index +  'div[1]/div[3]/p[1]/a[2]'
        
            item = d.find_element("xpath",xpath_item).text
            date = d.find_element("xpath",xpath_date).text
            star = d.find_element("xpath",xpath_star).text
               
            star_text = d.find_element("xpath",xpath_star_text).text
            review = d.find_element("xpath",xpath_review).text
        
        
            review_df.loc[df_cnt] = [item, date, star,star_text, review]
            df_cnt+=1
            print(df_cnt)
            sleep(2)
        except:
            print("error : No item")
            break
            #continue
        
    try:    
        next_page = d.find_element(By.CSS_SELECTOR, '#listPowerReview > div > a.now + a')
        next_page.click()
        page_loop+=1
        sleep(3)
        
    except:
        print("No next page")
        break

d.quit()
review_df.to_excel('review.xlsx')


# In[ ]:




