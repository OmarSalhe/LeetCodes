'''
You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box 
is empty, and '1' if it contains one ball.
    - balls initially separate
    - think arr instead of str

In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. 
Note that after doing so, there may be more than one ball in some boxes.
    - one ball at a time
    - total balls <= boxes
    - one unit = one adj box = 1 -> ops to any box = 1 * abs(i - j) = 1 unit * num of boxes

Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box.
    - assuming boxes form a linear path (non-circular), min ops = dist to box (or index)
    - only one target box per query
        - query = each index as the target

Each answer[i] is calculated considering the initial state of the boxes.
    - some value remains constant
        - empty boxes and starting positions

total dist = abs(i1 - j) + abs(i2 - j) + ... + abs(in - j)
           = abs(i1 + i2 + ... + in - j*n) -> for every non-empty box
           = abs(sum - j*n); sum = n*(n+1) / 2, but this fails to remove contributions from empty boxes
        -> = abs(sum - j * n - dist of empty boxes); dist of empty = sum of (empty indices + 1) - j * (num of empty boxes)

bugs out with boxes = "001011", indices 3, 4
because of symmetry -> some indices are negated. to offset, just split indices centered about j (so both sides remain positive)
eq doesn't change (i.e. abs(7-5) = abs(3-5)) so only change is to sum the intervals sep -> (prefix sum)

'''
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        prefix = [0] * (n + 1)
        not_empty = [0] * (n + 1)

        for i in range(1, n + 1):
            if boxes[i - 1] == '1':
                prefix[i] = i
                not_empty[i] = 1
            not_empty[i] += not_empty[i - 1]
            prefix[i] += prefix[i - 1]
        
        answer = [0] * n
        for i in range(1, n + 1):
            left = abs(prefix[i] - i * not_empty[i])
            right = prefix[n] - prefix[i] - i * (not_empty[n] - not_empty[i])
            answer[i - 1] = left + right
            print(left, right)
        return answer
