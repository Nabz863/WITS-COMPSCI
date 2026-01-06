# ===============================================================
# Assignment II - COMS4050/7057 (Discrete Optimization)
# Fiduccia & Mattheyses (FM) Algorithm with Penalty Function
# Due Date: 17 September 2025
# Student Name: Luke Renton
# Student number: 2540440
# ===============================================================

values = [6, 8, 3, 4, 5, 9, 11, 12, 6, 8, 13, 15, 16, 13, 9, 25]
weights = [3, 5, 4, 7, 4, 10, 3, 6, 8, 14, 4, 9, 10, 11, 17, 12]
W = 25
n = len(values)
R = 200  # (penalty strength)

# Initial solution: xi = 1 if i is odd (1-indexed), else 0
x = [1 if (i + 1) % 2 == 1 else 0 for i in range(n)]

def total_weight(x): return sum(w * xi for w, xi in zip(weights, x))
def total_value(x): return sum(v * xi for v, xi in zip(values, x))

def phi(x):
    """Penalty component: excess weight over capacity."""
    return max(0, total_weight(x) - W)

def fitness(x):
    """Fitness with R=200 penalty term."""
    return total_value(x) - R * phi(x)

x_best = x[:]
f_best = fitness(x)
flag = 1
Pass = 1

print("===============================================================")
print("FIDUCCIA & MATTHEYSES (FM) LOCAL SEARCH WITH PENALTY FUNCTION")
print("===============================================================")
print(f"Initial solution: x = {x}")
print(f"Initial weight = {total_weight(x)}, value = {total_value(x)}, fitness = {f_best:.2f}")
print("---------------------------------------------------------------")

while flag == 1:
    flag = 0
    Epoch = 0
    F = list(range(n))
    L = []
    x_epoch_best = x[:]
    f_epoch_best = fitness(x)

    print(f"\n=== PASS {Pass} START ===")

    while F:
        Epoch += 1
        best_gain = float('-inf')
        best_index = None

        for j in F:
            x_try = x[:]
            x_try[j] = 1 - x_try[j]
            gain = fitness(x_try) - fitness(x)
            if gain > best_gain:
                best_gain = gain
                best_index = j

        if best_index is None:
            break

        # Apply best flip
        x[best_index] = 1 - x[best_index]
        F.remove(best_index)
        L.append(best_index)
        f_curr = fitness(x)
        w_curr = total_weight(x)

        print(f"Epoch {Epoch:2d}: flipped index {best_index:2d}, "
              f"weight = {w_curr}, fitness = {f_curr:.2f}, gain = {best_gain:+.2f}")

        if f_curr > f_epoch_best:
            f_epoch_best = f_curr
            x_epoch_best = x[:]

    # End of pass
    if f_epoch_best > f_best:
        f_best = f_epoch_best
        x_best = x_epoch_best[:]
        x = x_best[:]
        flag = 1
        Pass += 1
        print(f"→ Improved global best: fitness = {f_best:.2f}, weight = {total_weight(x_best)}")
    else:
        print("→ No further improvement. Terminating search.")
        break

print("\n===============================================================")
print("FINAL RESULTS")
print("===============================================================")
print(f"Best solution x* = {x_best}")
print(f"Total weight = {total_weight(x_best)}")
print(f"Total value  = {total_value(x_best)}")
print(f"Final penalized fitness = {fitness(x_best):.2f}")
print("===============================================================")
