from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # price on first day
        buy = prices[0]
        profit = 0
        # start on day 2 cuz you alr on day 1
        for price in prices[1:]:
            # if a profit can be made
            if price >= buy:
                # make it
                profit += price - buy
                buy = price
            else:
                buy = price
        return profit