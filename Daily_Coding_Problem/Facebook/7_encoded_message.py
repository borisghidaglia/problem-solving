"""This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of
ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and
'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""
ALPHABET =set(str(i) for i in range(1,27))

def solve(msg):
    # Means that the entire message has been used, thus it is a possible decoding.
    if not msg:
        return 1

    # Look for the encoded letters in the alphabet that match the begining of the msg
    matches = [letter for letter in ALPHABET if msg[:len(letter)] == letter]
    # Given all the matches found, repeat the process for the remaining part of the msg
    recurse = [solve(msg[len(match):]) for match in matches]

    # Sum possible decodings
    return sum(recurse)

assert solve('111') == 3 #  'aaa', 'ka', 'ak'
assert solve('1212') == 5 # 'abab' , 'll', 'lab', 'abl', 'aub'
