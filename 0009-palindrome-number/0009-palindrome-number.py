class Solution(object):
    def isPalindrome(self, x):
        if x < 0: return 0
        
        x = str(x)
        for idx in range(len(x)/2):
            if x[idx] <> x[len(x)-1-idx]:
                return 0
        return 1