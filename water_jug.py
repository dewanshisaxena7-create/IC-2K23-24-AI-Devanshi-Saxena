
from collections import deque


def water_jug_solver(capacity_a, capacity_b, target):
    """Find a sequence of steps to measure the target quantity."""
    if capacity_a < 0 or capacity_b < 0 or target < 0:
        raise ValueError("Capacities and target cannot be negative.")

    if target > max(capacity_a, capacity_b):
        print("Target cannot be measured with these jug capacities.")
        return

    start = (0, 0)
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        (a, b), path = queue.popleft()

        if a == target or b == target:
            print("Solution found:")
            for step, state in enumerate(path):
                print(f"Step {step}: Jug A = {state[0]}, Jug B = {state[1]}")
            print("Total steps:", len(path) - 1)
            return path

        # Fill either jug
        next_states = [
            (capacity_a, b),
            (a, capacity_b),
            (0, b),
            (a, 0),
        ]

        # Pour A into B
        transfer = min(a, capacity_b - b)
        next_states.append((a - transfer, b + transfer))

        # Pour B into A
        transfer = min(b, capacity_a - a)
        next_states.append((a + transfer, b - transfer))

        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [state]))

    print("No solution exists for these inputs.")
    return None


if __name__ == "__main__":
    try:
        water_jug_solver(4, 3, 2)
    except ValueError as error:
        print("Invalid input:", error)
