class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        extra = sum(nums) - target
        if len(nums) <= 1 and extra == 0:
            return 1
        if extra % 2 == 1:
            return 0
        memo = {}
        def backtrack(total:int, target: int, i:int):
            if i == len(nums): return 1 if total == target else 0
            if (total, i) in memo: return memo[(total, i)]
            add = backtrack(total + nums[i], target, i + 1)
            sub = backtrack(total - nums[i], target, i + 1)
            memo[(total, i)] = add + sub
            return memo[(total, i)]
        return backtrack(0, target, 0)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        extra = sum(nums) - target
        if len(nums) <= 1 and extra == 0:
            return 1
        if extra % 2 == 1:
            return 0
        memo = {}
        def backtrack(total:int, target: int, i:int):
            if i == len(nums): return 1 if total == target else 0
            if (total, i) in memo: return memo[(total, i)]
            add = backtrack(total + nums[i], target, i + 1)
            sub = backtrack(total - nums[i], target, i + 1)
            memo[(total, i)] = add + sub
            return memo[(total, i)]
        return backtrack(0, target, 0)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        extra = sum(nums) - target
        if len(nums) <= 1 and extra == 0:
            return 1
        if extra % 2 == 1:
            return 0
        memo = {}
        def backtrack(total:int, target: int, i:int):
            if i == len(nums): return 1 if total == target else 0
            if (total, i) in memo: return memo[(total, i)]
            add = backtrack(total + nums[i], target, i + 1)
            sub = backtrack(total - nums[i], target, i + 1)
            memo[(total, i)] = add + sub
            return memo[(total, i)]
        return backtrack(0, target, 0)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        extra = sum(nums) - target
        if len(nums) <= 1 and extra == 0:
            return 1
        if extra % 2 == 1:
            return 0
        memo = {}
        def backtrack(total:int, target: int, i:int):
            if i == len(nums): return 1 if total == target else 0
            if (total, i) in memo: return memo[(total, i)]
            add = backtrack(total + nums[i], target, i + 1)
            sub = backtrack(total - nums[i], target, i + 1)
            memo[(total, i)] = add + sub
            return memo[(total, i)]
        return backtrack(0, target, 0)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        extra = sum(nums) - target
        if len(nums) <= 1 and extra == 0:
            return 1
        if extra % 2 == 1:
            return 0
        memo = {}
        def backtrack(total:int, target: int, i:int):
            if i == len(nums): return 1 if total == target else 0
            if (total, i) in memo: return memo[(total, i)]
            add = backtrack(total + nums[i], target, i + 1)
            sub = backtrack(total - nums[i], target, i + 1)
            memo[(total, i)] = add + sub
            return memo[(total, i)]
        return backtrack(0, target, 0)
