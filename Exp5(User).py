from collections import defaultdict, Counter
# Data
reviews = [
    ("fun, couple, love, love", "comedy"),
    ("fast, furious, shoot", "action"),
    ("couple, fly, fast, fun, fun", "comedy"),
    ("furious, shoot, shoot, fun", "action"),
    ("fly, fast, shoot, love", "action")
]
def tokenize(text):
    return text.split(", ")
def prod(iterable):
    result = 1
    for x in iterable:
        result *= x
    return result
# Prepare data
class_docs, class_count, vocabulary = defaultdict(list), defaultdict(int), set()
for review, category in reviews:
    tokens = tokenize(review)
    class_docs[category].extend(tokens)
    class_count[category] += 1
    vocabulary.update(tokens)
vocab_size = len(vocabulary)
priors = {cat: count / len(reviews) for cat, count in class_count.items()}
likelihoods = {cat: {word: (Counter(tokens)[word] + 1) / (len(tokens) + vocab_size) for word in vocabulary}
               for cat, tokens in class_docs.items()}
# Get user input
D = input("Enter a document: ")
tokens = tokenize(D)
posteriors = {cat: priors[cat] * prod(likelihoods[cat].get(token, 1 / (len(class_docs[cat]) + vocab_size)) for token in tokens)
              for cat in priors}
# Output
print('Posterior Probability:', posteriors)
print(f"The most likely class for the document '{D}' is: {max(posteriors, key=posteriors.get)}")
