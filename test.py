import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from collections import Counter

# Read the contents of the file
with open("paragraphs.txt") as file:
    para = file.read()

# Tokenize the text
words = nltk.word_tokenize(para)

# Remove stop words
stop_words = set(stopwords.words('english'))
filtered_words = [word.lower() for word in words if word.lower() not in stop_words]
# Count word frequency
word_freq = Counter(filtered_words)


# Display word frequency count
for word, freq in word_freq.items():
    print(f"{word}: {freq}")