def results(data, labels, centers):
    number_clusters = len(centers)  
    print(f'Results from {number_clusters} clusters:')

    for i in range(number_clusters):
        print(f'Representative points: {data.columns} for Group {i+1}:', 
        centers[i])

    counts = [len(data[labels == i]) for i in range(number_clusters)]
    print('Number of pupils in each group:', *counts)