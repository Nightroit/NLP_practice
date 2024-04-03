import nltk
from nltk.tokenize import word_tokenize 
from langdetect import detect 
import re

result = {}

nltk.download("punkt")

text = "Hoy tengo una importante meeting en la office. Excited to present our new product!"
seperators = "!,;+-~."

sentences = re.split('[' + re.escape(seperators) + ']', text)

# Filtering sentences
sentences = list(filter(lambda x : len(x) != 0, sentences))

for sentence in sentences:
    lang = detect(sentence)
    
    if lang not in result: 
        result[lang] = []

    tokenized_word = word_tokenize(sentence)
    tokenized_word = list(filter(lambda x : x not in seperators, tokenized_word))
    
    result[lang].append(tokenized_word)

print(result)