from gensim.models import Word2Vec
model = Word2Vec.load("D:/data/wiki2vector/en_1000_no_stem/en.model")
print(model.similarity('woman', 'man'))