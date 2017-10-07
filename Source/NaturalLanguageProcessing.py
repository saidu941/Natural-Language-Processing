import nltk
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')

import re
def tokens(text):
    """
    Get all words from the corpus
    """
    return re.findall('[a-z]+', text.lower())

WORDS = tokens(file('input.txt').read())
words1=open('input.txt').read()
print (WORDS)

#WORDNET
from nltk.corpus import wordnet as wn
print("\n\nWordNET: \n")
for WORD in WORDS:
    synsets= wn.synsets(WORD)
    print(str(syns.definition()) for syns in synsets)



#Tokenization
from nltk.tokenize import word_tokenize,wordpunct_tokenize,sent_tokenize
print("\n\n\n TOKENIZATION: \n")
print(sent_tokenize(words1))
print([word_tokenize(t) for t in sent_tokenize(words1)])



#Stemming
from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer
for WORD in WORDS:
    stemmer = PorterStemmer()
    print(WORD,stemmer.stem(WORD))




#POS
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
for WORD in WORDS:
    print(pos_tag(WORD))




#LEMMATIZATION
from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
for WORD in WORDS:
    print(WORD,lemmatizer.lemmatize(WORD))




#TRIGRAM
from nltk import word_tokenize
from nltk.util import ngrams

input_list = []
for WORD in WORDS:
    input_list=input_list+[WORD]
print(input_list)

def find_trigrams(input_list):
  trigram_list = []
  for i in range(len(input_list)-2):
      trigram_list.append((input_list[i], input_list[i+1],input_list[i+2]))
  return trigram_list
print(find_trigrams(input_list))





#NAMED ENTITY RECOGNITION
from nltk import word_tokenize, pos_tag, ne_chunk
for WORD in WORDS:
    print ne_chunk(pos_tag(WORD))