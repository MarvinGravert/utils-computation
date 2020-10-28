###GRPC init


# test()
###Generate DATA


#=>get x,y, label,center
###Apply kMeans

##=>
###send to server
#Prep data

#create stub

#receive Data 

#prepare for Checking

###Check data

##Plot Results
from typing import Tuple
import numpy as np

from sklearn.cluster import DBSCAN,KMeans
from sklearn import metrics
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from typing import List, Tuple,Dict
from sklearn.utils.validation import _num_samples

##settings
centers:List[Tuple[float,float]] = [[1, 1], [2, 1], [1, -1]]
numSamples:int=100
seed:int=0
# #############################################################################
# Generate sample data
points, clusterLabels ,clusterCenters= make_blobs(n_samples=numSamples, centers=centers, cluster_std=0.4,
                            random_state=seed,return_centers=True)
# X = StandardScaler().fit_transform(X)
base_test_solution:np.ndarray=np.hstack((points,clusterLabels.reshape(numSamples,1)))
###############
#compute kmeans
k_means=KMeans(n_clusters=4, random_state=0).fit_predict(points)
k_means_test_solution:np.ndarray=np.hstack((points,k_means.reshape(numSamples,1)))

# # #############################################################################
# # Compute DBSCAN
db_test = DBSCAN(eps=0.8, min_samples=30).fit(points)

dbScan_test_solution:np.ndarray=np.hstack((points,db_test.labels_.reshape(numSamples,1)))


# # Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(db_test.labels_)) - (1 if -1 in db_test.labels_ else 0)
n_noise_ = list(db_test.labels_).count(-1)

# #############################################################################
# Plot result
import matplotlib.pyplot as plt
plt.figure(1)
plt.title(label=f"k_means")
plt.scatter(points[:, 0], points[:, 1], c=k_means)
# # Black removed and is used for noise instead.
plt.figure(2)
plt.title(label=f"dbScan numClusters={n_clusters_}")
plt.scatter(points[:, 0], points[:, 1], c=db_test.labels_)
plt.show()




# unique_labels = set(labels)
# colors = [plt.cm.Spectral(each)
#           for each in np.linspace(0, 1, len(unique_labels))]
# for k, col in zip(unique_labels, colors):
#     if k == -1:
#         # Black used for noise.
#         col = [0, 0, 0, 1]

#     class_member_mask = (labels == k)

#     xy = points[class_member_mask & core_samples_mask]
#     plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
#              markeredgecolor='k', markersize=14)

#     xy = points[class_member_mask & ~core_samples_mask]
#     plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
#              markeredgecolor='k', markersize=6)

# plt.title('Estimated number of clusters: %d' % n_clusters_)
