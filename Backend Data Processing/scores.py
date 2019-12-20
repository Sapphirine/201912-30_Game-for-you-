import pandas as pd
df = pd.read_csv('/Users/ql/Desktop/info_with_score.csv')
score = pd.DataFrame(df, columns=['Title', 'Userscore'])
score.to_csv("/Users/ql/Desktop/game_score.csv", index=False)