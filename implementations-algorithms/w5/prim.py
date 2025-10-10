import heapq


def prim(graph, start):
    """
    Prim's algorithm to find the Minimum Spanning Tree (MST).

    :param graph: dict, adjacency list {node: [(neighbor, weight), ...]}
    :param start: starting vertex
    :return: (mst_edges, total_weight)
    """

    visited = set()  # Vertices already in MST
    mst_edges = []  # List of edges in MST
    total_weight = 0

    # Min-heap priority queue: (weight, u, v)
    pq = []

    # Start with edges from 'start'
    visited.add(start)
    for v, w in graph[start]:
        heapq.heappush(pq, (w, start, v))  # O(E log V) across algorithm

    while pq and len(visited) < len(graph):
        w, u, v = heapq.heappop(pq)  # O(log V)
        if v in visited:
            continue
        # Add edge to MST
        visited.add(v)
        mst_edges.append((u, v, w))
        total_weight += w

        # Add new edges from v
        for to, wt in graph[v]:
            if to not in visited:
                heapq.heappush(pq, (wt, v, to))

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

    mst, weight = prim(graph, 'A')

    print("Edges in MST:")
    for u, v, w in mst:
        print(f"{u} -- {v} ({w})")

    print(f"\nTotal weight of MST = {weight}")
