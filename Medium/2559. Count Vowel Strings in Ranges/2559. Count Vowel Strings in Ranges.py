'''
You are given a 0-indexed array of strings words and a 2D array of integers queries.
    - each index contains a single str
Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.
    - ri + 1 to include ri
    - if s[0], s[n-1] in vowel -> set
    - checking every range = O(n2) -> too slow, must know values before hand (preprocess) + a way to find values in a range (prefix sum)
Return an array ans of size queries.length, where ans[i] is the answer to the ith query.

Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.

len(words) = large -> O(n) needed

Approach:
    figure out # of strings encountered that start and end w/ vowel at every index -> single pass
        for ever str in words
            if end and start == vowl -> increment total so far
    for every query find the number of 'good' strings within that range; i.e. prefix[r] (total encountered) - prefix[l] (excluded portion)

TC = O(n) -> single pass
SC = O(n + m) -> prefix + output
'''
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n, m = len(words), len(queries)
        prefix = [0] * (n + 1)
        answer = [0] * m
        vowel = set(('a', 'e', 'i', 'o', 'u'))
        for i in range(1, n + 1):
            if words[i - 1][0] in vowel and words[i - 1][len(words[i - 1]) - 1] in vowel:
                prefix[i] += 1 
            prefix[i] += prefix[i - 1]
        
        for i in range(m):
            l, r = queries[i]
            answer[i] = prefix[r + 1] - prefix[l]
        return answer
