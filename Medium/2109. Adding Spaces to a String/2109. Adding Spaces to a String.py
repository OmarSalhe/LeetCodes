class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        out = []
        j = 0
        for i in range(len(spaces)):
            out.append(s[j:spaces[i]])
            out.append(' ')
            j = spaces[i]
        
        out.append(s[spaces[len(spaces) - 1]:])
    
        return ''.join(out)
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        out = []
        j = 0
        for i in range(len(spaces)):
            out.append(s[j:spaces[i]])
            out.append(' ')
            j = spaces[i]
        
        out.append(s[spaces[len(spaces) - 1]:])
    
        return ''.join(out)
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        out = []
        j = 0
        for i in range(len(spaces)):
            out.append(s[j:spaces[i]])
            out.append(' ')
            j = spaces[i]
        
        out.append(s[spaces[len(spaces) - 1]:])
    
        return ''.join(out)
