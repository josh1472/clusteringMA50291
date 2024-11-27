import matplotlib.pyplot as plt

def plot_clusters(data, centers, labels, n_clusters):
    # plots the clusters
    height = data.iloc[:, 0]
    weight = data.iloc[:, 1]
    plt.scatter(height, weight, c=labels, cmap='viridis')
    # plots the centers of the clusters
    plt.scatter(centers[:, 0], centers[:, 1], c='red')
    plt.title(f'K-Means Clustering with {n_clusters} clusters')
    # saves the plot
    plt.savefig(f'kmeans_{n_clusters}.png')
    # shows the plot
    plt.show()
    # closes the plot
    plt.close()
    