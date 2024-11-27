import pandas as pd
from clustering_package import (kmeans, readfile, results, statistics, plot_clusters, print_statistics, export_clusters)

if __name__ == "__main__":
    data = readfile('data_Borough_school.csv')
    mean, median, variance, std_dev = statistics(data)
    print_statistics(mean, median, variance, std_dev)
    for n_clusters in range(2, 6):
        centers, labels = kmeans(data, n_clusters)
        plot_clusters(data, centers, labels, n_clusters)

        export_clusters(data, labels, n_clusters, prefix=f'cluster_{n_clusters}')

    



    

