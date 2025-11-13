"""
Count distinct topological orderings of a DAG
"""

def count_topological_orderings(graph, in_degree):
    """
    Recursively count all distinct topological orderings.

    Args:
        graph: adjacency list {node: [neighbors]}
        in_degree: dict {node: in_degree_count}

    Returns:
        int: number of distinct topological orderings
    """
    # Base case: no nodes left
    if not in_degree:
        return 1

    # Find all nodes with in-degree 0 (can be placed next)
    available = [node for node, degree in in_degree.items() if degree == 0]

    if not available:
        # Should not happen in a valid DAG
        return 0

    total_count = 0

    # Try each available node as the next in ordering
    for node in available:
        # Create new state with this node removed
        new_in_degree = in_degree.copy()
        del new_in_degree[node]

        # Decrease in-degree for all neighbors
        if node in graph:
            for neighbor in graph[node]:
                if neighbor in new_in_degree:
                    new_in_degree[neighbor] -= 1

        # Recursively count orderings for remaining graph
        total_count += count_topological_orderings(graph, new_in_degree)

    return total_count


def enumerate_topological_orderings(graph, in_degree, current_ordering=[]):
    """
    Enumerate and print all distinct topological orderings.

    Args:
        graph: adjacency list {node: [neighbors]}
        in_degree: dict {node: in_degree_count}
        current_ordering: current partial ordering

    Returns:
        list of all orderings
    """
    # Base case: complete ordering
    if not in_degree:
        return [current_ordering[:]]

    # Find all nodes with in-degree 0
    available = [node for node, degree in in_degree.items() if degree == 0]

    all_orderings = []

    # Try each available node
    for node in available:
        # Add node to current ordering
        current_ordering.append(node)

        # Create new state
        new_in_degree = in_degree.copy()
        del new_in_degree[node]

        # Decrease in-degree for neighbors
        if node in graph:
            for neighbor in graph[node]:
                if neighbor in new_in_degree:
                    new_in_degree[neighbor] -= 1

        # Recursively get orderings
        all_orderings.extend(enumerate_topological_orderings(graph, new_in_degree, current_ordering))

        # Backtrack
        current_ordering.pop()

    return all_orderings


if __name__ == "__main__":
    # Define the graph from the image
    # Edges: A→B, B→E, C→D, D→E, E→F, E→H, F→G, G→I, H→I

    graph = {
        'A': ['B'],
        'B': ['E'],
        'C': ['D'],
        'D': ['E'],
        'E': ['F', 'H'],
        'F': ['G'],
        'G': ['I'],
        'H': ['I'],
        'I': []
    }

    # Calculate in-degrees
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    print("Graph structure:")
    print("Edges: A→B, B→E, C→D, D→E, E→F, E→H, F→G, G→I, H→I")
    print()

    print("In-degrees:")
    for node in sorted(in_degree.keys()):
        print(f"  {node}: {in_degree[node]}")
    print()

    # Count topological orderings
    count = count_topological_orderings(graph, in_degree.copy())
    print(f"Total number of distinct topological orderings: {count}")
    print()

    # Enumerate all orderings
    print("All distinct topological orderings:")
    orderings = enumerate_topological_orderings(graph, in_degree.copy(), [])
    for i, ordering in enumerate(orderings, 1):
        print(f"  {i:2d}. {' → '.join(ordering)}")
    print()
    print(f"Verification: {len(orderings)} orderings found")
