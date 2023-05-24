import nltk
#need to downlod this for first time
nltk.download('punkt')
from nltk.tokenize import word_tokenize

# Sample text for tokenization
text = "Hello, how are you doing today? I hope everything is going well."

# Tokenize the text
tokens = word_tokenize(text)

# Print the tokens
print(tokens)
