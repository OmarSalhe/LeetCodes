class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        digits[-1] += 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += carry
            if (digits[i]>= 10):
                carry = digits[i] // 10
                digits[i] %= 10
            else:
                carry = 0
                break
        if carry > 0:
            digits.insert(0, carry)
        return digits