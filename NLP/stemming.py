import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Sample text for stemming
text = "The cats are jumping over the fences."

# Tokenize the text
tokens = word_tokenize(text)

# Initialize PorterStemmer
stemmer = PorterStemmer()

# Perform stemming
stemmed_tokens = [stemmer.stem(token) for token in tokens]

# Print the stemmed tokens
print(stemmed_tokens)
