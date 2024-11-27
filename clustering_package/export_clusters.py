import pandas as pd
import numpy as np

def export_clusters(data, labels, n_clusters, prefix):

    for i in range(n_clusters):
        # Extract data points belonging to the current cluster
        cluster_data = data[labels == i]
        
        # Save the cluster data to a CSV file
        cluster_data.to_csv(f'{prefix}_cluster_{i+1}.csv', index=False)
    
    