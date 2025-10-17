import random
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cluster = None  
    def set_cluster(self, c):
        self.cluster = c


class KMeans:
    def __init__(self, num_points, num_clusters):
        self.num_points = num_points
        self.num_clusters = num_clusters
        self.points = []
        self.centroids = []
        self.cluster_groups = [] 
        self.start()

    def start(self):
        self.points = [Point(random.randint(0, self.num_points), random.randint(0, self.num_points))
                       for _ in range(self.num_points)]

        self.centroids = [Point(random.randint(0, self.num_points), random.randint(0, self.num_points))
                          for _ in range(self.num_clusters)]

        count = 0
        while True:
            for p in self.points:
                min_dist = float('inf')
                closest_cluster = 0
                for idx, c in enumerate(self.centroids):
                    dist = math.sqrt((c.x - p.x) ** 2 + (c.y - p.y) ** 2)
                    if dist < min_dist:
                        min_dist = dist
                        closest_cluster = idx
                p.set_cluster(closest_cluster)

            old_centroids = [Point(c.x, c.y) for c in self.centroids]

           
            for i in range(self.num_clusters):
                cluster_points = [p for p in self.points if p.cluster == i]
                if cluster_points:
                    avg_x = sum(p.x for p in cluster_points) / len(cluster_points)
                    avg_y = sum(p.y for p in cluster_points) / len(cluster_points)
                    self.centroids[i].x = int(avg_x)
                    self.centroids[i].y = int(avg_y)

            error = sum(abs(self.centroids[i].x - old_centroids[i].x) +
                        abs(self.centroids[i].y - old_centroids[i].y)
                        for i in range(self.num_clusters))

            count += 1
            if error == 0:
                break

        for i in range(self.num_clusters):
            intra_distance = 0
            for p in self.points:
                if p.cluster == i:
                    intra_distance += math.sqrt((self.centroids[i].x - p.x) ** 2 +
                                                (self.centroids[i].y - p.y) ** 2)
            print(f"Cluster {i + 1} Intra-distance = {intra_distance:.2f}")

        
        for i in range(self.num_clusters):
            for p in self.points:
                if p.cluster == i:
                    print(f"Point({p.x}, {p.y}) → Cluster {p.cluster + 1}")

        self.group_clusters()

    def group_clusters(self):
        cluster_sizes = [0] * self.num_clusters
        for p in self.points:
            cluster_sizes[p.cluster] += 1

        for i in range(self.num_clusters):
            cluster_points = [p for p in self.points if p.cluster == i]
            self.cluster_groups.append(cluster_points)

        print("\nClustering complete!\n")


if __name__ == "__main__":
    num_points = int(input("Insert number of points: "))
    num_clusters = int(input("Insert number of clusters: "))
    kmeans = KMeans(num_points, num_clusters)
