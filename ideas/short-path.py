from math import radians, cos, sin, asin, sqrt
from collections import defaultdict
import heapq as hq
from typing import *

def DD(a, b):
    (lat1, lon1), (lat2, lon2) = a, b
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * asin(sqrt(a))
    # Radius of earth in kilometers. Use 3956 for miles
    r = 6371
    # calculate the result
    return(c * r)


def build_adjacency(X: List[Tuple[str, Tuple[float, float]]]) -> DefaultDict[str, Set[Tuple[str, float]]]:
    # Build dictionary of distance between every two point
    B = {(x[0], y[0]): DD(x[1], y[1]) for x in X for y in X if x != y}
    #print(B)

    # treshold to consider two cities connected
    treshold = 300

    # only get pairs of cities within the treshold
    C = {x for x in B if B[x] <= treshold}

    # connect cities to their nearest cities regardless of treshold
    for x in X:
        mi, k = 7600, ""
        for y in X:
            if x == y:
                continue
            if (d := DD(x[1], y[1])) < mi:
                mi = d
                k = y[0]
        C.add((x[0], k))

    # Build the adjacency list (undirected)
    CC = set()
    D = defaultdict(set)
    for x in C:
        D[x[0]].add((x[1], B[(x[0], x[1])]))
        D[x[1]].add((x[0], B[(x[0], x[1])]))

    return D

# takes in Adjacency List, city a to city b and returns path
# returns -1 if there is no path found
def dist_city(A: DefaultDict[str, Set[Tuple[str, float]]], ca: str, cb: str) -> List[str]:
    if ca == cb:
        return 0

    # Dijkstra's algorithm
    pq = []
    hq.heappush(pq, (0, [ca]))
    while pq:
        t = hq.heappop(pq)
        # cc has the entire path till now
        cost, cc = t
        cur = cc[-1]
        if any([cc.count(x) > 1 for x in cc]):
            continue
        if cur == cb:
            return cc
        for nxt in A[cur]:
            hq.heappush(pq, (cost + nxt[1], cc + [nxt[0]]))

    return -1

# example to test
if __name__ == '__main__':
    X = [("Abuja", (9.072264 , 7.491302)),
            ("Dakar", (14.716677 , -17.467686)),
            ("Delhi", (28.7041, 77.1025)),
            ("Lucknow", (26.8467, 80.9462)),
            ("Chennai", (13.0827, 80.2707)),
            ("Puducherry", (11.9416, 79.8083)),
            ("Coimbatore", (11.0168, 76.9558)),
            ("Madurai", (9.9252, 78.1198)),
            ("Nagpur", (21.1458, 79.0882)),
            ("Mumbai", (19.0760, 72.8777)),
            ("Ahmedabad", (23.0225, 72.5714)),
            ("Surat", (21.1702, 72.8311)),
            ("Indore", (22.7196, 75.8577))]
    A = build_adjacency(X)

    print(dist_city(A, "Mumbai", "Nagpur"))
    print(dist_city(A, "Delhi", "Nagpur"))  # :(
