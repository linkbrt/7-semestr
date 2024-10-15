import numpy as np
import matplotlib.pyplot as plt


num_points = 100
num_clusters = 5
random_seed = 101

np.random.seed(random_seed)

points = np.random.rand(num_points, 2)

initial_centroids = points[np.random.choice(points.shape[0], num_clusters, replace=False)]

def k_means(points, initial_centroids, num_iterations=10):
    centroids = initial_centroids
    for iter in range(num_iterations):
        distances = np.linalg.norm(points[:, np.newaxis] - centroids, axis=2)
        labels = np.argmin(distances, axis=1)

        new_centroids = np.array([points[labels == i].mean(axis=0) for i in range(num_clusters)])
        centroids = new_centroids

        visualise(plt, points, centroids, labels)        
        plt.title(f'Итерация {iter + 1}')
        plt.pause(1)
        plt.clf()

    return labels, centroids


def visualise(plt, points, centroids, labels):
    plt.scatter(points[:, 0], points[:, 1], c=labels, cmap='viridis', marker='o')
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='x')


plt.figure(figsize=(10, 8))
labels, centroids = k_means(points, initial_centroids)

visualise(plt, points, centroids, labels)
plt.title('Final Clusters')
plt.show()
