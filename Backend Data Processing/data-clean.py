import pandas as pd
df = pd.read_csv('/Users/ql/Desktop/comments.csv', names=['Num', 'Title', 'Platform', 'Userscore', 'Comment', 'length'])
(x,y) = df.shape
for i in range(x):
    comment = str(df.iloc[i,4])
    cnt = len(comment.split())
    df.iloc[i,5] = cnt
res = df.query('length > 10').drop(['length'], axis=1)
res.to_csv("/Users/ql/Desktop/comments_clean.csv", index=False)