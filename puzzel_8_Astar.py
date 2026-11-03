import heapq

goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def h(s):
    return sum(abs(i//3-(v-1)//3) + abs(i%3-(v-1)%3)
               for i, v in enumerate(s) if v)

def astar(start):
    pq = [(h(start), 0, start, [])]
    seen = {}

    while pq:
        f, g, s, path = heapq.heappop(pq)

        if s in seen and seen[s] <= g:
            continue
        seen[s] = g

        if s == goal:
            for move, board in path:
                print("Move:", move)
                for i in range(0, 9, 3):
                    print(*["_" if x == 0 else x
                            for x in board[i:i+3]])
            print("Goal State Reached")
            print("Solution Cost =", g)
            return

        z = s.index(0)
        for move, d in [("UP", -3), ("DOWN", 3),
                        ("LEFT", -1), ("RIGHT", 1)]:
            n = z + d
            if not 0 <= n < 9:
                continue
            if move == "LEFT" and z % 3 == 0:
                continue
            if move == "RIGHT" and z % 3 == 2:
                continue

            a = list(s)
            a[z], a[n] = a[n], a[z]
            a = tuple(a)
            heapq.heappush(pq, (g + 1 + h(a), g + 1,
                                a, path + [(move, a)]))

    print("No solution exists")

print("Enter puzzle row by row (use 0 for blank):")
start = tuple(map(int, input().split()))
start += tuple(map(int, input().split()))
start += tuple(map(int, input().split()))

if len(start) != 9 or set(start) != set(range(9)):
    print("Invalid input!")
else:
    astar(start)