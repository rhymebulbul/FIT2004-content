import heapq


def dijkstra(graph, source):
    """
    Dijkstra's algorithm: Single source shortest paths for graphs with non-negative weights.

    :param graph: dict, adjacency list representation
                  {node: [(neighbor, weight), ...]}
    :param source: start vertex
    :return: dist, pred (shortest distances and predecessors)
    """

    # Initialize distances and predecessors
    dist = {v: float('inf') for v in graph}  # O(V)
    pred = {v: None for v in graph}  # O(V)
    dist[source] = 0  # O(1)

    # Priority queue: stores (distance, vertex)
    # Building heap from list is O(V)
    pq = [(0, source)]

    visited = set()  # Set of finalized nodes

    while pq:  # At most O(V) iterations
        # Extract min: O(log V) due to heap
        d, u = heapq.heappop(pq)

        if u in visited:  # Skip if already processed
            continue
        visited.add(u)

        # Relaxation step: each edge (u,v) processed once overall → O(E)
        for v, weight in graph[u]:
            # Relax edge if shorter path found
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight  # O(1)
                pred[v] = u  # O(1)
                # Update priority queue: O(log V)
                heapq.heappush(pq, (dist[v], v))

    return dist, pred


# ------------------ TEST CASES ------------------

if __name__ == "__main__":
    # Example from lecture notes:
    # Graph:
    #   A--10--B
    #   |5
    #   C--3--B
    #   |9
    #   D--6--E
    #   C--2--E
    #   B--1--D
    #   D--4--E

    graph = {
        'A': [('B', 10), ('C', 5)],
        'B': [('C', 3), ('D', 1)],
        'C': [('B', 3), ('D', 9), ('E', 2)],
        'D': [('E', 4)],
        'E': []
    }

    dist, pred = dijkstra(graph, 'A')

    print("Shortest distances from A:")
    for node in dist:
        print(f"{node}: {dist[node]}")

    print("\nPredecessors (shortest path tree):")
    for node in pred:
        print(f"{node}: {pred[node]}")
