class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        i, j = 0, 0
        word = 0
        while i < len(sentence):
            word += 1 # 1-indexed so start at 1
            while j < len(sentence) and j - i < len(searchWord) and sentence[j] == searchWord[j-i]:
                print(sentence[j])
                j += 1
            
            if j - i == len(searchWord):
                return word
            else:
                while j < len(sentence) and sentence[j] != ' ':
                    j += 1
            
            j += 1 # start on the first letter of word
            i = j # place i on the start of word
            

        return -1
