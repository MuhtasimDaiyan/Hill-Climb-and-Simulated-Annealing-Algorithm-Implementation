import random


# 1. Define the Objective Function
def objective_function(binary_string):
    """Calculates f = |13 * one(v) - 170|"""
    num_ones = sum(1 for bit in binary_string if bit == '1')
    return abs(13 * num_ones - 170)


# 2. Generate Initial Random Solution
def generate_initial_solution(length=40):
    return [random.choice(['0', '1']) for _ in range(length)]


# 3. Hill Climbing Algorithm
def hill_climbing(max_iterations=1000):
    # Start with a random solution
    current_solution = generate_initial_solution(40)
    current_value = objective_function(current_solution)

    for _ in range(max_iterations):
        # Generate neighbors by flipping one random bit
        neighbor = list(current_solution)
        idx_to_flip = random.randint(0, len(neighbor) - 1)
        neighbor[idx_to_flip] = '1' if neighbor[idx_to_flip] == '0' else '0'

        neighbor_value = objective_function(neighbor)

        # If neighbor is better, move to that neighbor
        if neighbor_value > current_value:
            current_solution = neighbor
            current_value = neighbor_value
        else:
            # If no better neighbor found (local peak), stop
            break

    return "".join(current_solution), current_value


# 4. Run with Random Restarts (to find global maximum)
best_overall_val = -1
best_overall_sol = None

for i in range(100):  # MAX = 100 resets
    sol, val = hill_climbing()
    if val > best_overall_val:
        best_overall_val = val
        best_overall_sol = sol
    print(f"Run {i + 1}: Local Max = {val}")

print(f"\nFinal Best Solution: {best_overall_sol}")
print(f"Maximum Value Found: {best_overall_val}")
