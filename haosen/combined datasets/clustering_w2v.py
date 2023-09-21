from gensim.models import Word2Vec
from sklearn.cluster import KMeans
import numpy as np

# Read labels and their corresponding values from a file
with open('raw.txt', 'r') as file:
    lines = file.readlines()

labels = [line.strip().split(':')[0] for line in lines]

# Word2Vec model
model = Word2Vec([labels], vector_size=100, window=5, min_count=1, sg=1)

# Get word vectors
word_vectors = [model.wv[label] for label in labels]

# Apply K-means clustering
kmeans = KMeans(n_clusters=10)  # You can adjust the number of clusters as needed
kmeans.fit(word_vectors)
clusters = kmeans.predict(word_vectors)

# Ccluster-label mapping
cluster_labels = {}
for label, cluster in zip(labels, clusters):
    if cluster not in cluster_labels:
        cluster_labels[cluster] = []
    cluster_labels[cluster].append(label)

# Write the results
with open('result_w2v.txt', 'w') as output_file:
    for cluster, labels in cluster_labels.items():
        labels_str = ', '.join(labels)
        output_file.write(f'Cluster {cluster}: {labels_str}\n')
