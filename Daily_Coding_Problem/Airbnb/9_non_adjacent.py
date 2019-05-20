"""This problem was asked by Airbnb.

Given a list of integers, write a function that returns
the largest sum of non-adjacent numbers. Numbers can
be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we
pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since
we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant
space?
"""

# Fully Recursive
def solve(l):
    if len(l) <= 2:
        return max(l)
    with_last = solve(l[:-2]) + l[-1]
    without = solve(l[:-1])
    return max(with_last, without)

# Dynamic Programming
def solve_linear(l):
    # if in store
    if store.get(len(l)): return store.get(len(l))
    # else
    if len(l) <= 2:
        return max(l)
    with_last = solve_linear(l[:-2]) + l[-1]
    without = solve_linear(l[:-1])
    best = max(with_last, without)
    store[len(l)] = best
    return best

# Iterative version
def solve_linear_it(l):
    max_before = None
    max_bbefore = None
    new_max = None
    for idx, elt in enumerate(l):

        if idx == 0:
            max_before = l[idx]
            continue

        if idx == 1:
            max_bbefore = max_before
            max_before = max(l[idx], l[idx-1])
            continue

        if not new_max:
            new_max = max(max_before, max_bbefore + l[idx])
            continue

        max_bbefore = max_before
        max_before = new_max

        new_max = max(max_before, max_bbefore + l[idx])


    return new_max


assert solve([2, 4, 6, 2, 5]) == 13
assert solve([5, 1, 1, 5]) == 10

store = {}
assert solve_linear([2, 4, 6, 2, 5]) == 13
store = {}
assert solve_linear([5, 1, 1, 5]) == 10

assert solve_linear_it([2, 4, 6, 2, 5]) == 13
assert solve_linear_it([5, 1, 1, 5]) == 10
