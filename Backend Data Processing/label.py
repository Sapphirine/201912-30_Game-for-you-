import pandas as pd
import nltk
import collections
from nltk import pos_tag, word_tokenize
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
df = pd.read_csv('/Users/ql/Desktop/comments_clean.csv')

game_label = {}
group = df.groupby('Title')
lemmatizer = WordNetLemmatizer()
useless_adj = ['black', 'such', 'poor', 'little', 'certain', 'obvious', 'read', 'unrecognizable', 'ol', 'i', 'high', 'understaffed', 'ready', 'near', 'someones', 'so-called', 'custom', 'other', 'good', 'gameplay', 'e', 'dead', 'из', 'wide', 'ive', 'fav', 'click', 'repetitive', 'capable', 'brown', 'whole', 'main', 'in-game', 'diablo', 'down', 'full', 'suppose', 'much', 'camo', 'only', 'few', 'suited', 'broken', 'god', 'open', 'last', 'halo', 'let', 'piss', 'similar', 'luigi', 'major', 'typical', 'true', 'advantage', 'false', 'own', 'different', 'uniform', 'una', 'plain', 'opposite', 'potential', 'diablo-ish', 'sorry', 'mentioned', 'real', 'previous', 'sub-par', 'bad', 'te', 'un', 'towards', 'many', 'na', 'due', 'allready', 'concerned', 'sure', 'tropical', 'missões', 'rusty', 'great', 'um', 'uma', 'ok', 'first', 'enough', 'next', 'game-type', '****', 'same', 'short', 'frequent', 'overall', 'exact', 'nice', 'able']

def helper(word):
    return lemmatizer.lemmatize(word, pos='a')

for game, g in group:
    com = ''
    (x, y) = g.shape
    for i in range(x):
        com += g.iloc[i, 4].lower()
    words = word_tokenize(com)
    words = list(map(helper, words))
    tmp = pos_tag(words)
    adj = []
    for w in tmp:
        if w[1] == 'JJ' and w[0] not in useless_adj:
            adj.append(w[0])
    labels = collections.Counter(adj).most_common(5)
    l = []
    for i in labels:
        l.append(i[0])
    game_label[game] = ','.join(l)

game_l = {}
game_l['Title'] = []
game_l['labels'] = []
for game in game_label:
    game_l['Title'].append(game)
    game_l['labels'].append(game_label[game])

g_label = pd.DataFrame(game_l)
g_label.to_csv("/Users/ql/Desktop/game_labels.csv", index=False)