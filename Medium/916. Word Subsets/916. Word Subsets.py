'''You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.
    - b is a subset of a iff freq1[i][k] >= freq2[j][k]
        - i.e. the frequency of letter k in k ,                                                                                                                                                                                                                                                                                                                                         the i/jth word

For example, "wrr" is a subset of "warrior" but is not a subset of "world".
    - does order matter? -> is 'rrw' a subset of 'warrior'

A string a from words1 is universal if for every string b in words2, b is a subset of a.
    - a is universal if b is always subset of a

Return an array of all the universal strings in words1. You may return the answer in any order.
    - len(universal) >= len(words1)


given two arrays: words1, words2; return all strs in words1 where any could form a str in words2

Decision:
words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
freq =  0 -> a=2, m=1, z=1, o=1, n=1
        1 -> a=1, p=2, l=1, e=1
        2 -> f=1, a=1, c=1, e=1, b=1, o=2, k=1
        3 -> g=2, o=2, l=1, e=1
        4 -> l=1, e=3, t=1, c=1, o=1, d=1
    
words2[0][0] -> apple, facebook, google, leetcode (i = 0 contains no e)
words2[1][0] -> amazon, facebook, google, leetcode (i = 1 contains no o)

only 3 match -> facebook, google, leetcode

can stop considering a string the moment it fails any
    - needs to have enough to accomodate all -> to be universal all str must contain max of all necessary letters in words2

store max freq of letters in words2 (freq1)
store freq of letters for all words in words1 (freq2)

if freq2[word][c] < freq1[c] -> can omit from univ
return remaining str'''
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        freq1 = []
        for word in words1: # build a table containing the frequency of every letter in each word of words1
            tmp = [0] * 26
            for c in word:
                tmp[ord(c) - ord('a')] += 1
            freq1.append(tmp)
        freq2 = []
        for word in words2: # same thing but for words2 now
            tmp = [0] * 26
            for c in word:
                tmp[ord(c) - ord('a')] += 1
            freq2.append(tmp)
        max_freq = [0] * 26
        for i in range(26): # condense the frequency table for words2 down to the max frequency for every letter
            cur_max = freq2[0][i]
            for j in range(1, len(words2)):
                cur_max = max(freq2[j][i], cur_max)
            max_freq[i] = cur_max
        univ = [i for i in range(len(words1))] # indices later used for selecting universal words
        for i in range(len(words1)): # for every word in words1
            for j in range(26):
                if freq1[i][j] < max_freq[j]: # check if enough letters occur to host all letters in words2
                    univ[i] = -1
                    break
        return [words1[i] for i in univ if i > -1] # exclude all marked strs
