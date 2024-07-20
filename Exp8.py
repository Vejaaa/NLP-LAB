import nltk
from nltk.corpus import wordnet
nltk.download('wordnet')
def get_synonyms_antonyms(word):
    synonyms, antonyms = set(), set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
            antonyms.update(ant.name() for ant in lemma.antonyms())
    return synonyms, antonyms
word = input("Enter a word: ")
synonyms, antonyms = get_synonyms_antonyms(word)
print(f"Synonyms: {', '.join(synonyms)}")
print(f"Antonyms: {', '.join(antonyms)}")
