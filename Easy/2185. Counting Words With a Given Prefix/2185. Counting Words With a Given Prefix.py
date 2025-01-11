'''
You are given an array of strings words and a string pref.

Return the number of strings in words that contain pref as a prefix.

A prefix of a string s is any leading contiguous substring of s.

prefix at start -> check first len(pref) letters

approach:
    for word in words:
        if pref matches first len(pref) letters in word:
            increment count

can do window check type of thing if slicing less intuitive
i.e.
    if pref[i] == word[j]:
        increment both
    else:
        don't match -> stop immediately
    
    if i == len(pref):
        letters matched len(pref) times AKA same words
'''

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words:
            if word[:len(pref)] == pref:
                count += 1
        return count
