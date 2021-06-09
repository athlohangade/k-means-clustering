import matplotlib.pyplot as plt

# using the make_blobs dataset
from sklearn.datasets.samples_generator import make_blobs
X, y = make_blobs(n_samples=200, centers=5, random_state=101)

# setting the number of training examples
all_points = [[i[0], i[1]] for i in X]
print(all_points)

plt.figure(figsize=(10,8))
plt.scatter(*zip(*all_points))
plt.title('Original Dataset')
plt.show()

# computing the initial centroids randomly
import random
K = 5

centroids = []
for k in range(K) :
  centroids.append(all_points[random.randint(0, len(all_points))])
print(centroids)

number_of_iterations = 10
for z in range(number_of_iterations) :
  cluster_points = [[] for x in range(K)]
  for i in range(len(all_points)) :
    temp_dist = [((all_points[i][0] - centroids[j][0]) ** 2 + (all_points[i][1] - centroids[j][1]) ** 2) ** 0.5 for j in range(K)]
    cluster_points[temp_dist.index(min(temp_dist))].append(all_points[i])

  for i in range(K) :
    sum_x = sum([j[0] for j in cluster_points[i]])
    sum_y = sum([j[1] for j in cluster_points[i]])
    centroids[i] = [sum_x / len(cluster_points[i]), sum_y / len(cluster_points[i])]

  plt.figure(figsize=(10,8))
  for i in range(K) :
    plt.scatter(*zip(*cluster_points[i]))
  plt.scatter(*zip(*centroids), s = 200, c='yellow')
  plt.show()
