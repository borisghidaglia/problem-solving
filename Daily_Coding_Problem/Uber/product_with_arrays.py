""" This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the
new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

def solve_with_div(array):
    """ Calculating the product of the entire array, which is O(n), and then dividing the total
    product by the value of each element, also O(n).

    That's O(n)
    """
    prod = 1
    for elt in array:
        prod*=elt

    return [prod/elt for elt in array]

def solve_brute_force(array):
    """ Iterating over each element in the array. Each time, we iterate through the array all
    over again and we multiply its elements by each other along the way, except for the
    element we are at in the first iteration.

    That's O(n^2)
    """
    res = []

    for x, elt in enumerate(array):
        local_prod = 1

        for y, val in enumerate(array):
            local_prod *= val if x != y else 1

        res.append(local_prod)
    return res

def solve(array):
    """ The idea is to store at the i th position the result of the product of every element
    before it in the array. By doing this from left to right and then from right to left, the last
    thing we have to do to compute the result is to iterate over the two created arrays and
    to multiply the corresponding elements ( aka the i th elements together)

    That's O(n)
    """
    left_right = [1 for elt in array]
    right_left = [1 for elt in array]

    nb_elements = len(array)
    for idx in range(1, nb_elements):
        left_right[idx] = array[idx - 1] * left_right[idx -1]
        right_left[nb_elements - idx - 1] = array[nb_elements - idx] * right_left[nb_elements - idx]

    return [lr * rl for lr, rl in zip(left_right, right_left)]

for func in [solve_with_div, solve_brute_force, solve]:
    assert func([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24], f"Error is comming from the {func.__name__} function !"
    assert func([3, 2, 1]) == [2, 3, 6], f"Error is comming from the {func.__name__} function !"
