import pandas as pd

labels = pd.read_csv('/Users/ql/Desktop/game_labels.csv')
info = pd.read_csv('/Users/ql/Desktop/info_with_score.csv')

res = pd.merge(info, labels, on='Title', how='left')
res.to_csv("/Users/ql/Desktop/info_score+labels.csv", index=False)