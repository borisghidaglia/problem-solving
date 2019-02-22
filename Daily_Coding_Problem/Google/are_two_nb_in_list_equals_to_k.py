# This problem was recently asked by Google.
#
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass? aka O(n)

short = [10, 15, 3, 7]
k = 17

vals = set()
# O(n)
def solve(array, k):
    # O(n)
    for elt in array:
        # O(1)
        if k - elt in vals:
            return True
        # O(1)
        vals.add(elt)

    return False


# True
assert solve([10, 15, 3, 7], 17)
# False
assert not solve([10, 15, 3, 4], 17)
# Empty array case
assert not solve([], 17)
# Duplicated vals case
assert solve([6, 6], 12)
