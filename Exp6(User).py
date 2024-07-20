import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from scipy.spatial.distance import euclidean, cityblock
from sklearn.metrics.pairwise import cosine_similarity
# Documents
docs = [
    "Shipment of gold damaged in a fire",
    "Delivery of silver arrived in a silver truck",
    "Shipment of gold arrived in a truck",
    "Purchased silver and gold arrived in a wooden truck",
    "The arrival of gold and silver shipment is delayed."
]
# User input for query
query = input("Enter a query: ")
# Vectorize
vec = CountVectorizer(stop_words="english") 
X = vec.fit_transform(docs + [query]).toarray()
doc_vecs, qry_vec = X[:-1], X[-1]
# Compute distances and similarities
euclidean_dists = [euclidean(doc, qry_vec) for doc in doc_vecs]
manhattan_dists = [cityblock(doc, qry_vec) for doc in doc_vecs]
cosine_sims = cosine_similarity(doc_vecs, qry_vec.reshape(1, -1)).flatten()
# Rankings
top_2_euclidean = np.argsort(euclidean_dists)[:2] + 1
top_2_manhattan = np.argsort(manhattan_dists)[:2] + 1
top_2_cosine = np.argsort(-cosine_sims)[:2] + 1
print("Euclidean Distances:", euclidean_dists)
print("Manhattan Distances:", manhattan_dists)
print("Cosine Similarities:", cosine_sims)
print("\nTop 2 docs (Euclidean):", top_2_euclidean)
print("Top 2 docs (Manhattan):", top_2_manhattan)
print("Top 2 docs (Cosine):", top_2_cosine)
