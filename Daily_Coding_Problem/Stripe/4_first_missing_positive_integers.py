""" This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

def solve(array):
    """ The idea is to use a set. For each element in the array, we add them in the set if they are
    positive (to save some time in the next step), and we refresh the min_val. That is O(n).
    Then if we didn't discovered a single positive value, we return 0 as it is the lowest integer.
    That is O(1). Finally, as long as we didn't returned something, we check if the min_val we
    found, plus 1, is in the array or not. If it is : we add one to our min value and we do the
    previous check again. If it is not, then it is our missing positive integer, thus we return it.
    """
    pos_vals = set()
    min_val = None

    for elt in array:
        if elt >= 0:
            pos_vals.add(elt)
            if min_val is None or elt < min_val : min_val = elt

    if not pos_vals:return 0

    while 1:
        if min_val+1 not in pos_vals: return min_val+1
        else : min_val += 1

assert solve([3, 4, -1, 1]) == 2
assert solve([0, 2, 1]) == 3
assert solve([-1, -1, -1]) == 0
