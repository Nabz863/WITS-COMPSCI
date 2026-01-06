# Distance matrix from the problem
M = [
    [0,   1.5, 3,   13, 3.5,  4.5, 1.5],
    [1.5, 0,   1.5, 1.3, 13,  13,  2.3],
    [3,   1.5, 0,   1.5, 3,   13,  3],
    [13,  1.3, 1.5, 0,   1.5, 13,  20],
    [3.5, 13,  3,   1.5, 0,   1.5, 3.3],
    [4.5, 13,  13,  13,  1.5, 0,   1.5],
    [1.5, 2.3, 3,   20,  3.3, 1.5, 0]
]

# Initial tour (given): x = (2, 7, 1, 4, 6, 5, 3)
initial_tour = [1, 6, 0, 3, 5, 4, 2]  # 0-based indexing

# Function to calculate total distance of a tour
def tour_cost(tour, dist_matrix):
    return sum(dist_matrix[tour[i]][tour[(i + 1) % len(tour)]] for i in range(len(tour)))

# 2-Opt implementation
def two_opt(tour, dist_matrix):
    n = len(tour)
    improving_solutions = []
    count = 0

    D = tour_cost(tour, dist_matrix)
    improved = True

    while improved:
        improved = False
        for i in range(n - 2):
            for j in range(i + 2, n if i > 0 else n - 1):
                new_tour = tour[:i+1] + tour[i+1:j+1][::-1] + tour[j+1:]
                new_cost = tour_cost(new_tour, dist_matrix)
                if new_cost < D:
                    tour = new_tour
                    D = new_cost
                    improving_solutions.append(([city + 1 for city in tour], D))  # 1-based for output
                    count += 1
                    improved = True
                    break
            if improved:
                break
    return [city + 1 for city in tour], D, improving_solutions, count

# Run the 2-Opt algorithm
final_tour, final_cost, improving_solutions, num_improvements = two_opt(initial_tour, M)

# Print results
print("Final Tour:", final_tour)
print("Final Cost:", final_cost)
print("Number of Improvements:", num_improvements)
print("Improving Solutions:")
for idx, (route, cost) in enumerate(improving_solutions):
    print(f" {idx+1}. Route: {route}, Cost: {cost}")
