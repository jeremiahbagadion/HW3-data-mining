# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "In hierarchical clustering methods such as single link, complete link, and group average, outliers or small groups of outliers tend to form singleton or small clusters that do not merge with other clusters until much later in the merging process. In k-means clustering, outliers can significantly distort the centroids of clusters, leading to less accurate clustering results​​."
    
    # type: bool (True/False)
    answers["(b)"] = True

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "This difference arises because agglomerative hierarchical clustering builds a cluster hierarchy that is deterministic, given the same starting conditions, and it does not rely on initial values that can change between runs. On the other hand, k-means clustering starts with a random initialization of centroids, which can lead to different solutions depending on the initial placement of these centroids​​."

    # type: bool (True/False)
    answers["(c)"] = False

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "Due to the complexity of O(m^2log(m)) for time and O(m^2) for space requirements​​, it is not accurate to claim that k-means is the most efficient clustering algorithm in all cases.  Other algorithms, such as density-based clustering (e.g., DBSCAN), can be more efficient and suitable depending on the context and the specific characteristics of the data."

    # type: bool (True/False)
    answers["(d)"] = True

    # type: explanatory string (at least four words)
    answers["(d) explain"] = "The Sum of Squared Errors (SSE) of the clustering decreases. This is because by introducing a new centroid closer to a subset of the clusters points, you are effectively reducing the total distance of those points from their nearest centroid, thereby lowering the overall SSE."

    # type: bool (True/False)
    answers["(e)"] = True

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "Whenever the Sum of Squared Errors (SSE) decreases in K-means clustering, cohesion increases. This relationship is due to the fact that SSE is a measure of cohesion itself, where a lower SSE indicates that points within a cluster are closer to the centroid, thereby implying higher cohesion within clusters."

    # type: bool (True/False)
    answers["(f)"] = True

    # type: explanatory string (at least four words)
    answers["(f) explain"] = "This is because SSB measures the variance between clusters, and a higher SSB value indicates that the clusters are more spread out from each other, hence more separated."

    # type: bool (True/False)
    answers["(g)"] = False

    # type: explanatory string (at least four words)
    answers["(g) explain"] = "Improving cohesion, which involves reducing the Sum of Squared Errors (SSE) within clusters, directly impacts the separation (larger between sum of squares, SSB), as these two metrics are inherently related. Specifically, minimizing SSE (improving cohesion) is equivalent to maximizing SSB (improving separation), given that the total sum of squares (TSS), which is a constant, is equal to the sum of SSE and SSB."

    # type: bool (True/False)
    answers["(h)"] = True

    # type: explanatory string (at least four words)
    answers["(h) explain"] = "This is because the total variance in the dataset can be decomposed into the variance within clusters (SSE) and the variance between clusters (BSS). The total variance is a fixed quantity based on the dataset, so if SSE decreases (meaning clusters become more tightly packed), BSS must increase to maintain the total variance constant, and vice versa."

    # type: bool (True/False)
    answers["(i)"] = False

    # type: explanatory string (at least four words)
    answers["(i) explain"] = "When cohesion increases, it means that the data points within a cluster are getting closer to their centroid, which reduces the SSE. However, this does not necessarily mean that the separation (SSB) will increase. In fact, its possible that increasing cohesion could lead to a decrease in separation if the clusters become too tight and start to overlap."

    return answers




# -----------------------------------------------------------
def question2():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "If the initial centroids are within the shaded circles and the distance between the circles is significantly larger than their radii, then all points within a circle will be closer to the centroid within that circle than to the centroid in the other circle. Therefore, when the k-means algorithm completes, each shaded circle will have one cluster centroid at its center."

    # type: bool (True/False)
    answers["(b)"] = False

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Given the spatial layout of the regions, it is likely that points on the inner edges of the crescents, which are closer to the centroid of the opposite crescent, will be assigned to the wrong cluster."

    # type: bool (True/False)
    answers["(c)"] = False

    # type: explanatory string (at least four words)
    answers["(c) explain"] = " There will not be an empty cluster, assuming standard k-means procedures are followed to handle any potential empty clusters during the iterations."

    return answers




# -----------------------------------------------------------
def question3():
    answers = {}

    # type: a string that evaluates to a float
    answers["(a) SSE"] = "4 * R ** 2"

    # type: a string that evaluates to a float
    answers["(b) SSE"] = "4 * (b**2 + a**2 + R**2 + 2*b*R + 2*a*R)"

    # type: a string that evaluates to a float
    answers["(c) SSE"] = "5 * R**2"

    return answers




# -----------------------------------------------------------
def question4():
    answers = {}

    # type: int
    answers["(a) Circle (a)"] = 0

    # type: int
    answers["(a) Circle (b)"] = 2

    # type: int
    answers["(a) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "No initial centroids in circle A and it has the same number of points as circle B but fewer than circle C, it is unlikely that a centroid will move into circle A. Given the proximity to circle C, it's quite likely that at least one centroid will move towards the dense population of points in circle C."

    # type: int
    answers["(b) Circle (a)"] = 1

    # type: int
    answers["(b) Circle (b)"] = 1

    # type: int
    answers["(b) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "The large number of points in circle C will attract the nearest centroids. It is highly likely that the centroid to the right in circle B will end up in circle C due to the mass of points pulling it."

    # type: int
    answers["(c) Circle (a)"] = 1

    # type: int
    answers["(c) Circle (b)"] = 0

    # type: int
    answers["(c) Circle (c)"] = 2

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "After K-means clustering, circle C will retain the majority of centroids due to its much higher point density, while circles A and B are likely to retain a centroid only if it was initially placed within them, given their equal size and distances."

    return answers




# -----------------------------------------------------------
def question5():
    answers = {}

    # type: set
    answers["(a)"] = set(["Group A", "Group B"])

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Group A and Group B have the shortest distance between any two points, thus according to single-link clustering, they should be merged."

    # type: set
    answers["(b)"] = set(["Group A", "Group C"])

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "The maximum distance between the most distant members of Group A and Group C is smaller than the maximum distance between the most distant members of any other pair of groups. This means that, even at their farthest points, Groups A and C are closer together than any other group combination, making them the best candidates for merging under the complete link criteria."

    return answers




# -----------------------------------------------------------
def question6():
    answers = {}

    # type: set
    answers["(a) core"] = set(["B", "C", "E", "F", "I", "J", "L", "M"])

    # type: set
    answers["(a) boundary"] = set(["D", "G"])

    # type: set
    answers["(a) noise"] = set(["A", "H"])

    # type: set
    answers["(b) cluster 1"] = set(["B", "C", "D", "E", "F", "G"])

    # type: set
    answers["(b) cluster 2"] = set(["I", "J", "L", "M"])

    # type: set
    answers["(b) cluster 3"] = set()

    # type: set
    answers["(b) cluster 4"] = set()

    # type: set
    answers["(c)-a core"] = set(["B", "C", "D", "E", "F", "G", "I", "J", "L", "M"])

    # type: set
    answers["(c)-a boundary"] = set(["A", "H"])

    # type: set
    answers["(c)-a noise"] = set()

    # type: set
    answers["(c)-b cluster 1"] = set(["A", "B", "C", "D", "E", "F", "G"])

    # type: set
    answers["(c)-b cluster 2"] = set(["H", "I", "J", "L", "M"])

    # type: set
    answers["(c)-b cluster 3"] = set()

    # type: set
    answers["(c)-b cluster 4"] = set()

    return answers




# -----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    answers["(a)"] = "Cluster 4"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Cluster 4 has the highest clustering entropy because it has the most balanced distribution of different classes, indicating a high degree of diversity and no single dominant class."

    # type: string
    answers["(b)"] = "Cluster 1"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Cluster 1 seems to be the most dominated by a single class, which is 'Water', with 30,000. A smaller entropy value indicates that the cluster's composition is less diverse and more orderly, with fewer land cover types sharing similar counts."

    return answers




# -----------------------------------------------------------
def question8():
    answers = {}

    # type: string
    answers["(a) Matrix 1"] = "Dataset Z"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 1"] = "The dark blue diagonal blocks indicate that the distance between points within the same cluster is very low, which is expected because the distance from any point to itself is zero, and points in the same cluster are very close to each other."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 1"] = "If the non-diagonal entries are significantly lighter or contain warmer colors such as red, it would indicate that the distance between points in different clusters is higher. This corresponds to the clear separation between clusters observed in Dataset Z, where each cluster is distinct and isolated from the others."

    # type: string
    answers["(a) Matrix 2"] = "Dataset X"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 2"] = "The uniform color along the diagonal entries suggests that points within each cluster are evenly spaced, as the clusters are arranged in a diagonal line from top left to bottom right. The tight packing of the central clusters would be indicated by darker colors along the diagonal, while the more spaced-out end clusters might show slightly lighter colors."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 2"] = "The symmetry in the non-diagonal entries likely reflects the structured and even spacing between the clusters in Dataset X."

    # type: string
    answers["(a) Matrix 3"] = "Dataset Y"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 3"] = "The varying intensity of colors along the diagonal from light blue to green suggests differences in the compactness of the clusters. The lighter colors may correspond to the bottom left clusters in Dataset Y, which are less tightly packed."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 3"] = "The variation in color intensity among the non-diagonal entries would reflect the irregular spacing and arrangement of the clusters in Dataset Y. Areas with warmer colors off the diagonal indicate greater distances between clusters."

    # type: string
    answers["(b) Row 1"] = "Cluster A"

    # type: string
    answers["(b) Row 2"] = "Cluster B"

    # type: string
    answers["(b) Row 3"] = "Cluster C"

    # type: string
    answers["(b) Row 4"] = "Cluster D"

    # type: explanatory string (at least four words)
    answers["(b) Row 1 explain"] = "Cluster A because the matrix should show larger distances within this cluster since the points are farther apart which would be represented by lighter colors in the corresponding row and column of the matrix."

    # type: explanatory string (at least four words)
    answers["(b) Row 2 explain"] = " Cluster B, which is tightly packed, meaning the distances within this cluster are short. This should be represented by darker colors in the matrix, indicating shorter distances."

    # type: explanatory string (at least four words)
    answers["(b) Row 3 explain"] = "Corresponds to Cluster C, also tightly packed, and would have a similar representation in the matrix as Cluster B with darker colors."

    # type: explanatory string (at least four words)
    answers["(b) Row 4 explain"] = "Matches with Cluster D for the same reasons as Cluster A, with lighter colors representing the larger distances between points within this cluster."

    return answers




# -----------------------------------------------------------
def question9():
    answers = {}

    # type: list
    answers["(a)"] = ["hierarchical", "overlapping", "partial"]

    # type: list
    answers["(b)"] = ["partitional", "exclusive", "complete"]

    # type: list
    answers["(c)"] = ["partitional", "exclusive", "complete"]

    # type: list
    answers["(d)"] = ["hierarchical", "overlapping", "partial"]

    # type: list
    answers["(e)"] = ["partitional", "exclusive", "complete"]

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "The clustering is partitional, exclusive, and complete because each student receives a unique letter grade that categorically places them into a distinct group, and all students in the course are assigned a grade."

    return answers




# -----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    answers["(a) Figure (a)"] = "No, clusters for features likely not detected with standard DBSCAN"

    # type: string
    answers["(a) Figure (b)"] = "Yes, clusters for features likely detected with appropriate DBSCAN"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "For figure (a), the features (eyes, nose, mouth) are less dense. The algorithm would likely identify the darker 'skin' as the primary cluster because of the high density of points. The eyes, nose, and mouth might be considered noise due to the lower density. For figure (b), the features are denser than their surroundings, and standard DBSCAN settings with a suitable ε and minPts are more likely to identify the features as distinct clusters."

    # type: string
    answers["(b) Figure (a)"] = "No"

    # type: string
    answers["(b) Figure (b)"] = "Yes, with appropriate K."

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "K-means clustering algorithm is not suitable for figure (a) because it assumes that clusters are isotropic and equally sized in the feature space. Since the facial features (eyes, nose, mouth) are represented by sparser points compared to the denser background 'skin', K-means would likely place centroids in the denser areas. For figure (b) since there are five features (two eyes, two parts of the mouth, and the nose), K should be set to 5. K-means would find the centroids of clusters based on the initial placement, which may or may not correspond exactly to the features depending on the initialization and distribution of points. K-means is sensitive to the initial starting conditions and may require several runs with different initializations to find a clustering that meaningfully represents the features."

    # type: string
    answers["(c)"] = "Hierarchical clustering"

    return answers

# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()
    print('end code')

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
