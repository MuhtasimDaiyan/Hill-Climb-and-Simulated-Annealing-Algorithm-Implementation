import numpy as np
import math
import random


# 1. Define the Objective Function (Maximize)
def objective_function(state):
    x0, x1, x2, x3 = state
    # Example equation with binary interaction
    return 12 * x0 + 16 * x1 + 22 * x2 + 8 * x3 - 10 * (x0 * x1 + x2 * x3)


# 2. Define Neighborhood Function (Flip one bit)
def get_neighbor(state):
    neighbor = list(state)
    index = random.randint(0, len(state) - 1)
    # Flip the chosen bit (0->1 or 1->0)
    neighbor[index] = 1 - neighbor[index]
    return tuple(neighbor)


# 3. Simulated Annealing Algorithm
def simulated_annealing(objective, initial_state, temp, cooling_rate, min_temp, iterations):
    current_state = initial_state
    current_eval = objective(current_state)
    best_state = current_state
    best_eval = current_eval

    while temp > min_temp:
        for _ in range(iterations):
            # Generate neighbor
            neighbor = get_neighbor(current_state)
            neighbor_eval = objective(neighbor)

            # Calculate acceptance probability
            # Note: For maximization, we use (new - old)
            diff = neighbor_eval - current_eval

            if diff > 0 or random.random() < math.exp(diff / temp):
                current_state = neighbor
                current_eval = neighbor_eval

                # Update global best
                if current_eval > best_eval:
                    best_state = neighbor
                    best_eval = neighbor_eval

        # Cool down
        temp *= cooling_rate

    return best_state, best_eval


# 4. Parameters and Execution
# Binary variables (4 variables)
initial_state = (0, 0, 0, 0)  # Start all off
temp = 1000
cooling_rate = 0.95
min_temp = 0.01
iterations = 100

best_sol, best_val = simulated_annealing(
    objective_function, initial_state, temp, cooling_rate, min_temp, iterations
)

print(f"Best Binary Solution: {best_sol}")
print(f"Maximum Value: {best_val}")
