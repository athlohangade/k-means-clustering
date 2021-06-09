# K-Means Clustering

## Theory 

Clustering is the process of collecting or grouping similar data objects based on the information found
in the data that describes the object and their relationships.
The set of objects in the same group or cluster are more similar to each other than to those in other groups or clusters.

There are many techniques by which clustering can be done.
One such algorithm is K-Means Clustering algorithm.
It is an iterative algorithm that aims to partition *n* data objects into *k* clusters in which each object belongs to the cluster with the nearest cluster centers or cluster centroid.
The centroid of the cluster is typically the mean of all the points in the cluster. The closeness of the point is measured by Euclidean distance between the point and the cluster center, but there are other metrics like Manhattan distance, cosine similarity, etc.

## Working

Given *k*, the K-Means algorithm works as follows :
1.  Choose k random data points (seeds) to be the initial centroids, i.e. the cluster centers.
2.  Assign each data point to the closest centroid.
3.  Re-compute the centroids using the current cluster memberships.
4.  If the convergence criterion is not met, repeat steps 2 and 3. We can say the algorithm has converged if there is no re-assignment of data points to different clusters in a particular iteration.

For more information on K-Means clustering algorithm, refer [wiki](https://en.wikipedia.org/wiki/K-means_clustering). For an explanation with a working example, refer `example.pdf`.

**Requirements** : MatplotLib, Scikit-learn
