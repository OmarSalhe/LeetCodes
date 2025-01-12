from typing import List
'''
Given an array of string words, return all strings in words that is a substring of another word.
You can return the answer in any order.
    - return word if word is found in another word

A substring is a contiguous sequence of characters within a string
    - sub < main
    - ltrs are consecutive

len(words), len(words[i]) = small -> bf allowed
bf = search for word in every word = O(n * m)
'''
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        s = ' '.join(words)
        return [word for word in words if s.count(word) > 1]
