"""This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list
add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass? aka O(n)
"""

def solve(array, k):
    """ The idea is to use a set.
    First, we have to create an empty set.
    Then, for each element in the array, if its complementary value is in the set, then return
    true. Otherwise, we add the element in the set. 
    """
    vals = set()

    for elt in array:
        if k - elt in vals:
            return True
        vals.add(elt)

    return False


assert solve([10, 15, 3, 7], 17)
assert not solve([10, 15, 3, 4], 17)
assert not solve([], 17)
assert solve([6, 6], 12)
