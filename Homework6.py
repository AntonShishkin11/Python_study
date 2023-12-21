#!/usr/bin/env python
# coding: utf-8

# In[6]:


import json
i = 0
purchases = {}
with open('purchase_log.txt', 'r', encoding = 'utf-8') as f:
    for line in f:
        line = line.strip()

        dict_ = json.loads(line)
        key = dict_['user_id']
        value = dict_['category']
        purchases[key] = value
        
for user_id, category in list(purchases.items())[:2]:
    print(f"{user_id} '{category}'")


# In[16]:


i = 0

with open('visit_log.csv', 'r', encoding='utf-8') as f:
    with open('purchase_log.txt', 'r', encoding='utf-8') as purchases:
        with open('funnel.csv', 'w', encoding='utf-8') as funnel:
            funnel.write('user_id,source,category\n')
            
            for line in purchases:
                purchase_data = {line.strip().split(',')[0]: line.strip().split(',')[1]}
            
                i += 1
                print(purchase_data, type(purchase_data))
                print(line)
                if i > 4:
                    break
            for line in f:
                user_id, source = line.strip().split(',')
                if user_id in purchase_data:
                    funnel.write(f'{user_id},{source},{purchase_data[user_id]}\n')
                    


# In[ ]:




