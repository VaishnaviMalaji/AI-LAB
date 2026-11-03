
import heapq

def a_star(graph, heuristic, start, goal):
    if start not in graph:
        print("Invalid start node!")
        return

    if goal not in graph:
        print("Goal node does not exist!")
        return

    pq = [(heuristic[start], 0, start)]
    g = {start: 0}
    parent = {start: None}

    while pq:
        f, cost, current = heapq.heappop(pq)

        if cost != g[current]:
            continue

        if current == goal:
            path = []
            node = goal

            while node is not None:
                path.append(node)
                node = parent[node]

            print("Optimal Path:", " -> ".join(path[::-1]))
            print("Total Cost:", g[goal])
            return

        for neighbour, weight in graph[current].items():
            new_cost = g[current] + weight

            if new_cost < g.get(neighbour, float('inf')):
                g[neighbour] = new_cost
                parent[neighbour] = current
                heapq.heappush(
                    pq, (new_cost + heuristic[neighbour],
                         new_cost, neighbour)
                )

    print("No path exists!")


# Base graph
base_graph = {
    'A': {'B': 1, 'C': 2, 'H': 7},
    'B': {'D': 4, 'E': 6},
    'C': {'F': 3, 'G': 2},
    'D': {'E': 7},
    'E': {},
    'F': {'H': 1},
    'G': {'H': 2},
    'H': {}
}

base_heuristic = {
    'A': 5, 'B': 3, 'C': 4, 'D': 2,
    'E': 6, 'F': 3, 'G': 1, 'H': 0
}

# Test case 6 graph
graph6 = {
    'A': {'B': 2},
    'B': {'A': 2},
    'C': {}
}

heuristic6 = {'A': 2, 'B': 1, 'C': 0}


# Execute all 8 test cases
for i in range(1, 9):
    print("\n========== TEST CASE", i, "==========")

    if i == 6:
        graph = graph6
        heuristic = heuristic6
    else:
        graph = base_graph
        heuristic = base_heuristic

    print("Available nodes:", list(graph.keys()))

    start = input("Enter start node: ").strip().upper()
    goal = input("Enter goal node: ").strip().upper()

    print("\nResult:")
    a_star(graph, heuristic, start, goal)

print("\n========== ALL TEST CASES COMPLETED ==========")
