import pandas as pd
df = pd.read_csv('/Users/ql/Desktop/info_score+labels.csv')
(x,y) = df.shape
dic1 = {}
dic2 = {}
res = {}
for i in range(x):
    name = df.iloc[i, 1]
    c = list(set(df.iloc[i, 4].split(';')))
    l = str(df.iloc[i, 8])
    if not l:
        continue
    dic1[name] = l.split(',')
    dic2[name] = c
for g in dic1:
    tmp = {}
    label = dic1[g]
    classes = dic2[g]
    for lab in label:
        for other_g in dic1:
            if other_g != g and lab in dic1[other_g]:
                if other_g in tmp:
                    tmp[other_g] += 2
                else:
                    tmp[other_g] = 2
    for lab in classes:
        for other_g in dic2:
            if other_g != g and lab in dic2[other_g]:
                if other_g in tmp:
                    tmp[other_g] += 1
                else:
                    tmp[other_g] = 1
    rec_g = sorted(tmp, key=lambda k: k[1], reverse=True)
    if len(rec_g) > 5:
        rec_g = rec_g[:5]
    res[g] = ','.join(rec_g)

game_rec = {}
game_rec['Title'] = []
game_rec['recommendation'] = []
for game in res:
    game_rec['Title'].append(game)
    game_rec['recommendation'].append(res[game])
g_label = pd.DataFrame(game_rec)
g_label.to_csv("/Users/ql/Desktop/game_rec.csv", index=False)