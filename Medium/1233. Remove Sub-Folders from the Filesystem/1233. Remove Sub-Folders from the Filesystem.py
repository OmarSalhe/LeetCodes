from typing import List

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # 0 = root folders, 1 = sub-folders
        folders = {f: 0 for f in folder}
        
        # increments all subfolders by 1
        for folder in folders:
            for i in range(1, len(folder)):
                if folder[i] == '/':
                    root = folder[:i]
                    if root in folders:
                        folders[folder] += 1
                        break

        return [f for f in folders if folders[f] == 0]

        # Time Complexity = O(n * m), where n = # of folders m = # of letters in each folder's name
        # Space Complexity = O(n), same size as the input
