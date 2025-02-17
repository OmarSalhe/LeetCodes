class Solution:
    def compressedString(self, word: str) -> str:
        n = len(word)
        comp = []

        i = 0
        while i < n:
            count = 0
            j = i
            while j < n and word[j] == word[i] and j - i < 9:
                j += 1
            
            count += j - i
            comp.append(f'{count}')
            comp.append(word[i])
            i = j 

        return "".join(comp)

"""
TC = O(n) -> single-pass
SC = O(n) -> worst case is only 1 letter streaks formed, therefore every letter has two ouputs 
            when compressed.
                i.e. abc = 1a1b1c
                
converted the instructions into more optimal code

instructions:
Begin with an empty string comp. 
While word is not empty, use the following operation:
    Remove a maximum length prefix of word made of a single character c repeating at most 9 times. 
    Append the length of the prefix followed by c to comp.
Return the string comp.

"""
