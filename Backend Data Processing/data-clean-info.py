import pandas as pd
df = pd.read_csv('/Users/ql/Desktop/info.csv', names=['Num', 'Title','Year','Publisher','Genre','Platform','Metascore','Avg_Userscore','No_Players'])
res = df.drop(['Metascore'], axis=1)
res = res.drop(['Avg_Userscore'], axis=1)
res.to_csv("/Users/ql/Desktop/info_clean.csv", index=False)