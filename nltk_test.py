"""NLTK Test"""
import nltk

sentence = """Over the centuries, the castle walls have crumbled."""

tokens = nltk.word_tokenize(sentence)
print(tokens)
print(nltk.pos_tag(tokens))
