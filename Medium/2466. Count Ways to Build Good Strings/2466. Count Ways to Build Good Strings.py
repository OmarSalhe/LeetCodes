'''
Given the integers zero, one, low, and high, we can construct a string by starting with an empty 
string, and then at each step perform either of the following:

Append the character '0' zero times.
Append the character '1' one times.
This can be performed any number of times.
    - must append all at once
        i.e. if one = 5, zero = 1 -> append 1 = 11111
    - if one, zero > high, cannot use respective number
        - 1 <= zero, one <= low -> dont need to worry

A good string is a string constructed by the above process having a length between low and high (inclusive).
    - consider all strs low ≤ len ≤ high

Return the number of different good strings that can be constructed satisfying these properties.
    - order of strs matter -> no dups
        - keep track of strs made -> if sim
        - use combinatorics -> handles dups BUT factorials

Since the answer can be large, return it modulo 109 + 7.
    - applied at the end

goal: form all possible bit strs from len high -> low, containing zero 0s and one 1s, and return the amount % 1000000007

Topics:
    - counting/combinations
        - how many possibility per index -> count[i] = count[i-1] * possibility; 0 <= possibility <= 2
    - combinatorics
        - how many ways can one fit into [low, high]?

1 <= low <= high <= 10**5
    - O(n) approach needed, sim too slow
    - (high - low) = 10***5 - 1 wc, range too large to iterate


low = 3, high = 3, zero = 1, one = 1
Decision (sim):
    if len > high: stop
    count = 1 if cur bit str >= low else 0

    append one 1 (if len + one <= high) -> len += one, append 0/1 (if ...)
    append zero 0 (if len + zero <= high) -> len += zero, append 0/1 (if ...)


_ _ _ -> each slot can be either zero/one so 2*2*2 -> why? if none chosen one/zero can fit in low=high=3 spots

low = 3, high = 3, zero = 1, one = 1
Decision (counting):
    if one + i <= high:
        count[i] += count[i-1]
    if zero + i <= high:
        count[i] += count[i-1]
    
    if neither:
        break -> if none can fit at that point, none can fit later
    
    sum all count[i]s where low - 1 < i < high
'''

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        count = [0] * (high + 1)
        count[0] = 1

        res = 0
        for i in range(1, high + 1):
            count[i] = ((count[i-one] if i >= one else 0) + (count[i-zero] if i>=zero else 0)) % 1000000007
            if i >= low and i <= high:
                res = (res + count[i])% 1000000007
        return res

        #     if i - one > -1: count[i] += count[i - one]
        #     if i - zero > -1: count[i] += count[i - zero]
        #     if i >= low:
        #         res += count[i]
        # return res % 1000000007

        # @cache
        # def count_cont(length: int, low: int, high: int, one: int, zero: int):
        #     if length > high: return 0

        #     count = 1 if length >= low else 0

        #     add_one = 0
        #     if one + length <= high:
        #         add_one = count_cont(length + one, low, high, one, zero) % 1000000007

        #     add_zero = 0
        #     if zero + length <= high:
        #         add_zero = count_cont(length + zero, low, high, one, zero) % 1000000007
            
        #     count += add_one + add_zero
        #     return count % 1000000007

        # return count_cont(0, low, high, zero, one)
