
def hill_climbing(graph, values, initial_state):
    if initial_state not in graph or initial_state not in values:
        print("Invalid initial state!")
        return

    current = initial_state

    while graph[current]:
        best = current

        for neighbour in graph[current]:
            if values[neighbour] > values[best]:
                best = neighbour

        if best == current:
            break

        current = best

    print("Final State:", current)
    print("Final Value:", values[current])


g1 = {'A':['B','C'], 'B':['D','E'], 'C':['F','G'],
      'D':[], 'E':[], 'F':[], 'G':[]}
v1 = {'A':2, 'B':4, 'C':5, 'D':7, 'E':6, 'F':8, 'G':9}

g2 = {'A':['B','C'], 'B':[], 'C':[]}
v2 = {'A':10, 'B':5, 'C':7}

g3 = {'A':['B'], 'B':[]}
v3 = {'A':3, 'B':8}

g4 = {'A':['B','C'], 'B':['D'], 'C':['E'], 'D':[], 'E':[]}
v4 = {'A':3, 'B':8, 'C':5, 'D':6, 'E':10}

g5 = {'A':['B','C'], 'B':[], 'C':[]}
v5 = {'A':5, 'B':5, 'C':5}

g6 = {'A':['B','C'], 'B':[], 'C':[]}
v6 = {'A':9, 'B':6, 'C':4}

g7 = {'A':['B','C','D'], 'B':[], 'C':[], 'D':[]}
v7 = {'A':2, 'B':5, 'C':9, 'D':7}

g8 = {'A':[]}
v8 = {'A':5}

g9 = {'A':['B'], 'B':[]}
v9 = {'A':3, 'B':8}

g10 = {'A':['B','C'], 'B':['D'], 'C':['E'],
       'D':[], 'E':[]}
v10 = {'A':2, 'B':8, 'C':4, 'D':6, 'E':10}

tests = [
    (g1,v1), (g2,v2), (g3,v3), (g4,v4), (g5,v5),
    (g6,v6), (g7,v7), (g8,v8), (g9,v9), (g10,v10)
]

for i, (graph, values) in enumerate(tests, 1):
    print("\n--- Test Case", i, "---")
    print("Available nodes:", list(graph.keys()))
    start = input("Enter initial state: ").strip().upper()
    hill_climbing(graph, values, start)

print("\nAll test cases completed!")
