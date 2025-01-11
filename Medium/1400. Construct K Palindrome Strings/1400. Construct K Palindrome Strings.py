'''
Given a string s and an integer k, return true if you can use all the characters
in s to construct k palindrome strings or false otherwise.
    - palindrome = symmetric
        - each letter (except center in odd case) must occur at least twice
        i.e. len(pal) -> even: all letters occur twice
                      -> odd: all letters occur twice except for one
    - palindromes don't need to match
        i.e. can derive at least one palindrome from an existing palindrome
        e.g pal = acbca becomes b, acca
                = acca becomes aa, cc
            - could be used recur on an existing palindrome
    - if k == n, all letters can be used to form palindrome
    - something to do with letter occurences
    - how to know if a palindrome forms:
        - all letters can form pairs with an outlier of one

Decision:
s = "annabelle", k = 2
pairs = a, n, e, l
single = b

k = 2 -> pop b -> k = 1 -> no singles remain, resulting str is a palindrome


s = "leetcode", k = 3
pairs = e
single = l, t, c, o, d

len(single) > k -> impossible to form k palindromes from cur str

Generalized:
get freq of every letter

for f in freq:
    pairs += count pairs in f
    single += count remainder after pairing

if single - 1 > k : -> subtract by one since you can designate one individual letter to still form a valid pal
    impossible
else:
    possible

TC = O(n)
SC = O(26)

test on s = abacdc, k = 2
pair = a, c
single = b, d

single - 1 < k -> possible
'''

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        nums = Counter(s)
        n = len(s)

        odd_n = sum(v & 1 for v in nums.values()) # count of numbers with a 1 bit -> odd numbers -> single numbers
        if k > n: # if not enough letters
            return False
        if k == n: # if enough letters
            return True

        if odd_n > k: # if too many single numbers to form a valid palindrome
            return False
        return True
