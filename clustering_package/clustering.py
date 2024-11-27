from sklearn.cluster import KMeans

def kmeans(data, n_clusters = 2):
    # creates the kmeans object
    kmeans = KMeans(n_clusters)
    # fits the data
    kmeans.fit(data)
    # gets the centers of the clusters
    centers = kmeans.cluster_centers_
    # gets the labels of the clusters
    labels = kmeans.labels_
    # returns the kmeans object and the labels
    return centers, labels


