
def depth_limited_search(node, goal, graph, limit, path):
    if node == goal:
        return path + [node]

    if limit == 0:
        return "cutoff"

    cutoff_occurred = False

    for child in graph.get(node, []):
        if child not in path:
            result = depth_limited_search(
                child, goal, graph, limit - 1, path + [node]
            )

            if isinstance(result, list):
                return result

            if result == "cutoff":
                cutoff_occurred = True

    if cutoff_occurred:
        return "cutoff"

    return "failure"


def iterative_deepening_search(initial, goal, graph, maximum_depth):
    for depth in range(maximum_depth + 1):
        result = depth_limited_search(
            initial, goal, graph, depth, []
        )

        if isinstance(result, list):
            return result

    return None


# User input
initial = input("Enter initial state: ").strip()
goal = input("Enter goal state: ").strip()
maximum_depth = int(input("Enter maximum depth: "))

n = int(input("Enter number of nodes: "))
graph = {}

print("Enter each node and its children separated by spaces.")
print("If a node has no children, enter -")

for _ in range(n):
    node, *children = input("Enter node and children: ").split()

    if children == ['-']:
        children = []

    graph[node] = children

# Perform IDS
result = iterative_deepening_search(
    initial, goal, graph, maximum_depth
)

# Display result
if result is not None:
    print("Goal found!")
    print("Solution path:", " -> ".join(result))
else:
    print("Goal not found within maximum depth.")
