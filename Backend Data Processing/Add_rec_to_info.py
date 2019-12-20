import pandas as pd

rec = pd.read_csv('/Users/ql/Desktop/game_rec.csv')
info = pd.read_csv('/Users/ql/Desktop/info_score+labels.csv')

res = pd.merge(info, rec, on='Title', how='left')
res.to_csv("/Users/ql/Desktop/info_complete.csv", index=False)