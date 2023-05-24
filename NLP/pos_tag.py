import nltk
#download this package for initial run and it should work
# nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

# Sample text for POS tagging
text = "I am learning Python programming."

# Tokenize the text
tokens = word_tokenize(text)

# Perform POS tagging
pos_tags = pos_tag(tokens)

# Print the POS tagged tokens
for token, pos in pos_tags:
    print(token, "-", pos)
