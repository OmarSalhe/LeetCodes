class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True

        tmp = x
        rev = 0
        while tmp:
            rev = (rev * 10) + tmp % 10
            tmp //= 10

        return rev == x
