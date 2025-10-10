class UnionFindNaive:
    def __init__(self, n):
        self.parent = list(range(n))  # parent[i] = i initially

    def find(self, u):
        """Return the root (set ID) of u by following parent pointers."""
        while self.parent[u] != u:
            u = self.parent[u]
        return u

    def union(self, u, v):
        """Join sets containing u and v."""
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_v] = root_u  # arbitrary choice


class UnionFind:
    def __init__(self, n):
        # parent[i] < 0 means i is root and |parent[i]| = size of the set
        # parent[i] >= 0 means parent[i] is the parent of i
        self.parent = [-1] * n

    def find(self, u):
        """Return the root of u by following parent pointers (no compression yet)."""
        while self.parent[u] >= 0:  # while not a root
            u = self.parent[u]
        return u

    def union(self, u, v):
        """Union by size."""
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False  # already in same set

        # Attach smaller tree to larger tree
        if self.parent[root_u] < self.parent[root_v]:  # root_u tree is bigger (remember sizes are negative!)
            self.parent[root_u] += self.parent[root_v]  # increase size
            self.parent[root_v] = root_u
        else:
            self.parent[root_v] += self.parent[root_u]
            self.parent[root_u] = root_v
        return True


def kruskal(n, edges):
    """
    Kruskal's algorithm using Union-Find.
    :param n: number of vertices (0..n-1)
    :param edges: list of (weight, u, v)
    """
    uf = UnionFind(n)  # or UnionFindPC(n) for path compression
    mst = []
    total_weight = 0

    for w, u, v in sorted(edges):  # sort by weight
        if uf.union(u, v):  # only add if no cycle
            mst.append((u, v, w))
            total_weight += w
            if len(mst) == n - 1:
                break
    return mst, total_weight


# ---------------- Example ----------------
if __name__ == "__main__":
    edges = [
        (10, 0, 1), (5, 0, 2),
        (3, 1, 2), (1, 1, 3),
        (9, 2, 3), (2, 2, 4),
        (4, 3, 4)
    ]
    mst, weight = kruskal(5, edges)
    print("MST edges:", mst)
    print("Total weight:", weight)
