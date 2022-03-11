#!/usr/bin/env python
# coding: utf-8

# In[9]:


def case_count(word):
    uppercase, lowercase = 0, 0
    for i in word:
        if i.isupper():
            uppercase += 1
        elif i.islower():
            lowercase += 1

    print("Uppercase:" + str(uppercase), "Lowercase:" + str(lowercase))


case_count("Hi Jordan")


# In[ ]:





# In[26]:


months = {"January":1,"February":2,"March":3,"April":4,
"May":5,"June":6,"July":7,"August":8,
"September":9,"October":10,"November":11,"December":12}

def date_passed(todays_date, scheduled_date):
    
    today_day = int(todays_date.split(" ")[0][:-2])
    today_month = months[todays_date.split(" ")[1]]
    
    s_day = int(scheduled_date.split(" ")[0][:-2])
    s_month = months[scheduled_date.split(" ")[1]]
    
    t_total = today_month * 30 + today_day
    s_total = s_month * 30 + s_day
    
    return t_total > s_total
    

print(date_passed("21st February", "21st February"))


# In[ ]:





# In[ ]:




