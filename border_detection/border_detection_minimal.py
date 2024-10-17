# border_detection_minimal.py

import numpy as np

def calculate_distances_close(x, p, close):
    """
    Calculate the average distance to the closest 'close' points for each point in the dataset.
    
    Parameters:
    x : np.ndarray
        The dataset (n_samples, n_features).
    p : int
        The norm to use for distance calculation (default is Euclidean norm, p=2).
    close : int
        The number of nearest points to consider for distance calculation.
    
    Returns:
    distances : np.ndarray
        The array of average distances to the closest 'close' points.
    """
    n_samples = x.shape[0]
    distances = np.zeros(n_samples)

    for i in range(n_samples):
        dist_list = []
        for j in range(n_samples):
            if i != j:
                dist = np.linalg.norm(x[i] - x[j], ord=p)
                dist_list.append(dist)

        # Sort the distances and select the top 'close' closest points
        dist_list.sort()
        top_close_dists = dist_list[:close]

        # Calculate the average of these top 'close' distances
        distances[i] = sum(top_close_dists) / close

    return distances

def classify_border_and_core_points(X, p=2, close=100, percentile=60):
    """
    Classify the points in the dataset as 'border' or 'core' based on the distance percentile.
    
    Parameters:
    X : np.ndarray
        The dataset (n_samples, n_features).
    p : int
        The norm to use for distance calculation (default is Euclidean norm, p=2).
    close : int
        The number of closest points to consider for the distance calculation (default=100).
    percentile : float
        The threshold percentile for defining border points (default=60).
    
    Returns:
    border_points : np.ndarray
        Points classified as 'border'.
    core_points : np.ndarray
        Points classified as 'core'.
    """
    # Calculate distances based on the closest 'close' points
    distances = calculate_distances_close(X, p, close)
    
    # Calculate the distance threshold for border points
    threshold_distance = np.percentile(distances, percentile)
    
    # Classify points as border or core based on the threshold
    border_points = X[distances >= threshold_distance]
    core_points = X[distances < threshold_distance]
    
    return border_points, core_points
