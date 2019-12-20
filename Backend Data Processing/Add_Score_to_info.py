import pandas as pd
pd.set_option('display.max_columns', None)

c = pd.read_csv('/Users/ql/Desktop/comments_clean.csv')
info = pd.read_csv('/Users/ql/Desktop/info_clean.csv')

group = c.groupby('Title')
s = group['Userscore'].agg('mean').reset_index()
s['Userscore']=s['Userscore'].round(decimals=2)
res = pd.merge(info, s, on='Title', how='left')
res.to_csv("/Users/ql/Desktop/infor_with_score.csv", index=False)