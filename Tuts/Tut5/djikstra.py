from typing import List, Tuple
import heapq

inf = float("inf")
# Graph is represented as an adjacency matrix
graph = [
    [0, 4, 2, 6, 8],
    [inf, 0, inf, 4, 3],
    [inf, inf, 0, 1, inf],
    [inf, 1, inf, 0, 3],
    [inf, inf, inf, inf, 0]
]

class PriorityQueue:
    def __init__(self, array: list[tuple]):
        if not all(isinstance(item, tuple) for item in array):
            raise TypeError("PriorityQueue must be initialized with a list of tuples.")
        self.pq = array
        # Each tuple of the pq is of type (node, d[v]) where d[v] is the distance of node
    def extractCheapest(self):
        # Each tuple of the pq is of type (node, d[v]) where d[v] is the distance of node
        min = float("inf")
        min_index = None

        for index in range(len(self.pq)):
            if self.pq[index][1] < min:
                min, min_index = self.pq[index][1], index

        
        # return self.pq.pop(min_index)[0]
        # instead of popping in middle, exchange the element with one at any edge and pop to make the whole operation cheaper
        # order doesnt matter in the pq as a data struct so we can afford to do this

        self.pq[min_index], self.pq[-1] = self.pq[-1], self.pq[min_index]
        # return the minimum node
        return self.pq.pop(-1)[0]
    
    def insert(self, pair:tuple):
        # Insert operation is kept simple(not inserting in an order because this
        # inserting happens way more often while updating distance values in djikstra
        # compared to extract_cheapest, so we keep this operation O(1) and that as O(V)
        self.pq.append(pair)
        return
    
    def remove_by_node(self, node: int):
        index = 0
        for index in range(len(self.pq)):
            if self.pq[index][0] == node:
                break
        self.pq[index], self.pq[-1] = self.pq[-1], self.pq[index]
        # return the minimum node
        self.pq.pop(-1)
        return

def dijkstra(graph, start):
    # List of nodes is determined by the length of adjacency matrix
    V = [i for i in range(1, len(graph)+1)]
    d, S, pi = [float("inf")]*len(V), [0]*len(V), [None]*len(V)
    d[start-1] = 0
    constructor = [(vertex, d[vertex-1]) for vertex in V]
    PQ = PriorityQueue(constructor)
    while len(PQ.pq) > 0:
        u = PQ.extractCheapest() # u is the next node to be added to set of visited nodes
        S[u-1] = 1
        for node in range(1, len(graph)+1):
            if node != u and graph[u-1][node-1]!= float("inf") and S[node-1] == 0 and d[node-1] > d[u-1] + graph[u-1][node-1]:
                d[node-1] = d[u-1] + graph[u-1][node-1]
                PQ.remove_by_node(node)
                PQ.insert((node, d[node-1]))
                pi[node-1] = u
    
    # Now, we have completed list of distances from starting node
        print(d)
        print(pi)

dijkstra(graph, 1)


