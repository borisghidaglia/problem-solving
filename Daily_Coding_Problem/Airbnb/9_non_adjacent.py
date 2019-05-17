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

# Iterative dynamic programming version linear time and constant space
def solve_linear_it(l):
    max_before = (None, None)
    max_bbefore = (None, None)
    for idx, elt in enumerate(l):

        if not max_before[0]:
            max_before = (elt, idx)
            continue

        if not max_bbefore[0]:
            if elt > max_before[0]:
                max_before, max_bbefore = (elt, idx), max_before
                continue
            else: max_bbefore = max_before; continue

        if elt + max_before[0] > max_before[0] and idx - max_before[1] > 1:
            max_before, max_bbefore = (max_before[0] + elt, idx), max_before
        elif elt + max_bbefore[0] > max_before[0]:
            max_before, max_bbefore = (elt + max_bbefore[0], idx), max_before

    return max_before[0]


assert solve([2, 4, 6, 2, 5]) == 13
assert solve([5, 1, 1, 5]) == 10

store = {}
assert solve_linear([2, 4, 6, 2, 5]) == 13
store = {}
assert solve_linear([5, 1, 1, 5]) == 10

assert solve_linear_it([2, 4, 6, 2, 5]) == 13
assert solve_linear_it([5, 1, 1, 5]) == 10
