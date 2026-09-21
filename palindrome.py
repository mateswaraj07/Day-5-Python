class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = x
        reverse = 0
        if x<0:
            return False
        else:
            while x!=0:
                digit = x % 10
                reverse = reverse*10+digit
                x = x//10
            if reverse == original:
                return True
            else:
                return False
s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(-121))
print(s.isPalindrome(10))