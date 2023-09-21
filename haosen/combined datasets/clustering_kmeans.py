from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import re

# Read labels from the file
def read_labels_from_file(file_path):
    labels = []
    with open(file_path, 'r') as file:
        for line in file:
            match = re.search(r'(\w+):\s\d+', line)
            if match:
                labels.append(match.group(1))
    return labels

# Perform K-means clustering
def kmeans_clustering(labels, num_clusters):
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(labels)
    
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(tfidf_matrix)
    
    return kmeans.labels_

# Group labels by cluster
def group_labels_by_cluster(labels, cluster_labels):
    grouped_labels = {}
    for label, cluster_label in zip(labels, cluster_labels):
        if cluster_label not in grouped_labels:
            grouped_labels[cluster_label] = []
        grouped_labels[cluster_label].append(label)
    return grouped_labels

file_path = 'raw.txt'  
num_clusters = 20  

labels = read_labels_from_file(file_path)
cluster_labels = kmeans_clustering(labels, num_clusters)
grouped_labels = group_labels_by_cluster(labels, cluster_labels)


for cluster_label, cluster in grouped_labels.items():
    print(f'Cluster {cluster_label + 1}:')
    print(', '.join(cluster))

with open('kmeans_result.txt', 'w') as output_file:
    for label, cluster in grouped_labels.items():
        output_file.write(f'{label}: Cluster {cluster}\n')