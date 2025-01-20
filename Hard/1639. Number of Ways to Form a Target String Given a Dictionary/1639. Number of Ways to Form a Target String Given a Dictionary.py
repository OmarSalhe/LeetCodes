'''
You are given a list of strings of the same length words and a string target.
    - len(words[i]) = n

Your task is to form target using the given words under the following rules:
    target should be formed from left to right.

    To form the ith character of target, you can choose the kth character of
    the jth string in words if target[i] = words[j][k].
        - 

    Once you use the kth character of the jth string of words, you can no longer use
    the xth character of any string in words where x <= k. In other words, all characters to the left of or
    at index k become unusuable for every string.
        - reduces number of letters available per choice
            - must reduce losses to ensure letter availability
            - must use the first occurence of letter to have other letters to access
        - cannot use the same kth letter since x <= k
    
    Repeat the process until you form the string target.
        - max of len(target) choices to be made; len(target) <= n

Notice that you can use multiple characters from the same string in words provided the conditions above are met.
    - can use the same word as long as you remove the char used and chars prior

Return the number of ways to form target from words. Since the answer may be too large, return it modulo 109 + 7.
    - can use diff words as starting points/sources of chars -> (branching)


len(words) -> small (O(n2) approach works)

(0-indexed)

goal: return number of ways to form target using chars in words while following condition


words = ["acca","bbbb","caca"], target = "aba"
start w/ i = 0

Decision:
stop if no more letters available (j == n)
stop if target is formed (k == len(target))

for i words to go through:
    if word[i][j] == target[k]: choose i -> remove first j letters, find k + 1

return



TC = O(n*m* len(target)) -> n*m possible letters to go through * len(target) letters to find
'''
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        @cache
        def find_next_ltr(j: int, k: int) -> int:
            if k == len(target): return 1 # handles bother cases where target forms (all ltrs exhausted or not)
            if j == len(words[0]): return 0 # all ltrs are exhausted and target did not form

            formed = 0 # number of ways target forms at this point
            for i in range(len(words)):
                for x in range(j, len(words[0])):
                    if words[i][x] == target[k]:
                        formed += find_next_ltr(x + 1, k + 1) # x + 1 to exclude up to jth ltr

            return formed % (7 + 10**9)
        
        return find_next_ltr(0, 0)
