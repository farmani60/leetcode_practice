
# Given a 32-bit signed integer, reverse digits of an integer.
# Example 1:
# Input: 123
# Output:  321

# Assume we are dealing with an environment which could only 
# hold integers within the 32-bit signed integer range. 
# For the purpose of this problem, assume that your function 
# returns 0 when the reversed integer overflows.

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        n = cmp(x, 0) * int(str(abs(x)))[::-1]
        return n if n.bit_length() < 32 else 0