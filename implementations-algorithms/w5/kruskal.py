class UnionFind:
    """Disjoint Set Union (Union-Find) with path compression and union by rank."""

    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])  # Path compression
        return self.parent[v]

    def union(self, u, v):
        root_u, root_v = self.find(u), self.find(v)
        if root_u == root_v:
            return False  # Already in the same set
        # Union by rank
        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        elif self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1
        return True


def kruskal(graph):
    """
    Kruskal's algorithm to find MST.

    :param graph: dict adjacency list {node: [(neighbor, weight), ...]}
    :return: (mst_edges, total_weight)
    """
    # Step 1: Extract all edges
    edges = []
    for u in graph:
        for v, w in graph[u]:
            if (v, u, w) not in edges:  # Avoid duplicates in undirected graph
                edges.append((u, v, w))

    # Step 2: Sort edges by weight
    edges.sort(key=lambda x: x[2])  # O(E log E)

    # Step 3: Initialize DSU
    uf = UnionFind(graph.keys())

    mst_edges = []
    total_weight = 0

    # Step 4: Process edges in increasing weight
    for u, v, w in edges:
        if uf.union(u, v):  # If u and v are in different sets
            mst_edges.append((u, v, w))
            total_weight += w
        if len(mst_edges) == len(graph) - 1:  # MST complete
            break

    return mst_edges, total_weight


# ------------------ TEST CASE ------------------
if __name__ == "__main__":
    graph = {
        'A': [('B', 10), ('C', 5)],
        'B': [('A', 10), ('C', 3), ('D', 1)],
        'C': [('A', 5), ('B', 3), ('D', 9), ('E', 2)],
        'D': [('B', 1), ('C', 9), ('E', 4)],
        'E': [('C', 2), ('D', 4)]
    }

    mst, weight = kruskal(graph)

    print("Edges in MST:")
    for u, v, w in mst:
        print(f"{u} -- {v} ({w})")

    print(f"\nTotal weight of MST = {weight}")
