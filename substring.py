# Given a string, find the length of the longest substring
# without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. 
# Note that the answer must be a substring, "pwke" is a subsequence
# and not a substring.



def allUnique(s, start, end):
    set = ""
    for i in range(start, end):
        ch = s[i]
        if ch in set:
            return False
        set += ch
    return True

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        ans = 0
        for i in range(n-1):
            for j in range(i+1, n):
                if allUnique(s, i, j):
                    ans = max(ans, j-i)
        return ans




if __name__ == '__main__':
    s = 'abcabcefgh'
    ans = Solution().lengthOfLongestSubstring(s)
    print(ans)


