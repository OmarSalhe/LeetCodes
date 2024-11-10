from collections import List, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = defaultdict(list)
        for s in strs:
            k = ''.join(sorted(s))
            ana[k].append(s)
        return [ana[k] for k in ana]
