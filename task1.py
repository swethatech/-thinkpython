import unittest
import test
import requests
import pandas as pd


data=requests.get('https://api.github.com/users')
data=data.json()

user_login=[]
user_id=[]
user_name=[]
follower_id=[]
follower_login=[]

for id in range(len(data)):
    d1=data[id]
    if d1['id']%10==0:
        info=requests.get(d1['url'])
        info=info.json()
        fol_info = requests.get(info['followers_url'])
        fol_info = fol_info.json()
        for j in range(len(fol_info)):
            d2 = fol_info[j]
            follower_id.append(d2['id'])
            follower_login.append(d2['login'])
            user_login.append(info['login'])
            user_id.append(info['id'])
            user_name.append(info['name'])
pd.DataFrame({'User Id':user_id,'User Login':user_login,'User Name':user_name,'Follower ID':follower_id,'Follower Login':follower_login}).to_csv('file.csv')

print('Required csv file has been created successfully.')
