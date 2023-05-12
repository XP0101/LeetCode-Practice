class Solution:
    def longestPalindrome(self, s):
        longest_palindrome = ""
        for center_idx in range(len(s)):
            for offset in [0, 1]:
                start_idx, end_idx = center_idx, center_idx + offset
                while True:
                    if start_idx < 0 or end_idx > len(s) - 1 or s[start_idx] != s[end_idx]:
                        break
                    else:
                        palin = s[start_idx:end_idx+1]
                        longest_palindrome = palin if len(palin) > len(longest_palindrome) else longest_palindrome   
                        start_idx -= 1
                        end_idx += 1
        return longest_palindrome