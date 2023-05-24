import nltk
# nltk.download('wordnet')
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Sample text for lemmatization
text = "the cats are jumping over the fence"

# Tokenize the text
tokens = word_tokenize(text)

# Initialize WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

# Perform lemmatization
lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]

# Print the lemmatized tokens
print(lemmatized_tokens)
