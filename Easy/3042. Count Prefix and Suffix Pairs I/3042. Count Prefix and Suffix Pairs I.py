'''
You are given a 0-indexed string array words.

Let's define a boolean function isPrefixAndSuffix that takes two strings, str1 and str2:

isPrefixAndSuffix(str1, str2) returns true if str1 is both a 
prefix and a suffix of str2, and false otherwise.
    - same pattern at start + end
    - str1 is given -> pattern is given
    - str1 must be smaller than str 2

For example, isPrefixAndSuffix("aba", "ababa") is true because "aba" is a prefix of "ababa" and also a suffix,
but isPrefixAndSuffix("abc", "abcd") is false.
    - prefix and suffix can intersect / don't need to be distinct

Return an integer denoting the number of index pairs (i, j) such that i < j, and isPrefixAndSuffix(words[i], words[j]) is true.
    - only one pair in list
    - guaranteed that str1 comes before str2

make isPrefixAndSuffix -> use as condition to find pair -> return number of pairs found

isPrefixAndSuffix defn:
    use two windows (one at start and other at end):
        if both left and right window == eachother and target -> expand window
        else -> stop (return False)

        repeat until window of len(target) reached
        return True

len(words), len(words[i]) = small -> O(n2) allowed

no way of knowing which str is str2 and can't sort since order matters so bf
bf = for every str:
        cur = current str
        for every str before cur:
            if len(cur) < len(str) and isPrefixAndSuffix is True:
                count_of_pair ++
    return count_of_pair
'''

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        count_of_pairs = 0
        for i in range(n):
            for j in range(i + 1, n):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    count_of_pairs += 1
        return count_of_pairs
