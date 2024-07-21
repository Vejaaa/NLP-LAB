from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
# Data
reviews = [
    ("fun, couple, love, love", "comedy"),
    ("fast, furious, shoot", "action"),
    ("couple, fly, fast, fun, fun", "comedy"),
    ("furious, shoot, shoot, fun", "action"),
    ("fly, fast, shoot, love", "action")
]
D = "fast, couple, shoot, fly"
# Prepare data
texts, labels = zip(*reviews)
# Create and fit the model
model = make_pipeline(CountVectorizer(tokenizer=lambda x: x.split(', ')), MultinomialNB())
model.fit(texts, labels)
# Predict the class and probabilities
predicted_class = model.predict([D])[0]
probabilities = model.predict_proba([D])[0]
# Output results
print(f"Predicted class for '{D}': {predicted_class}")
print(f"Class probabilities: {dict(zip(model.classes_, probabilities))}")
