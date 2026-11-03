
import math
import random

def objective(x):
    return (x - 3) ** 2

def simulated_annealing(initial_state, temperature, cooling_rate,
                        minimum_temperature, maximum_iterations, seed):
    random.seed(seed)

    current = initial_state
    current_cost = objective(current)
    best = current
    best_cost = current_cost

    for _ in range(maximum_iterations):
        if temperature <= minimum_temperature:
            break

        candidate = current + random.uniform(-1, 1)
        candidate_cost = objective(candidate)
        delta = candidate_cost - current_cost

        if delta < 0 or random.random() < math.exp(-delta / temperature):
            current = candidate
            current_cost = candidate_cost

            if current_cost < best_cost:
                best = current
                best_cost = current_cost

        temperature *= cooling_rate

    print("Best State (x):", format(best, ".6f"))
    print("Minimum Function Value:", format(best_cost, ".8f"))


tests = [
    (3, 100, 0.95, 0.01, 500, 1),
    (-5, 100, 0.95, 0.01, 500, 42),
    (9, 100, 0.95, 0.01, 500, 7),
    (0, 1, 0.9, 0.01, 500, 10),
    (10, 100, 0.5, 0.01, 100, 21)
]

for i, test in enumerate(tests, 1):
    print("\n--- Test Case", i, "---")
    print("Parameters:", test)

    initial = float(input("Enter initial state: "))
    temp = float(input("Enter initial temperature: "))
    rate = float(input("Enter cooling rate: "))
    minimum = float(input("Enter minimum temperature: "))
    iterations = int(input("Enter maximum iterations: "))
    seed = int(input("Enter random seed: "))

    simulated_annealing(initial, temp, rate, minimum, iterations, seed)

print("\nAll test cases completed!")
