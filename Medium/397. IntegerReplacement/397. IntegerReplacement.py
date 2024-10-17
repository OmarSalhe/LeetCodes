class Solution:
    def integerReplacement(self, n: int) -> int:
        res = 0
        while n>0:
            # if even
            if n%2==0:
                n//=2
            else:
                # if bit rep does not contain 2 or is three
                if n==3 or n&2==0:
                    n-=1 
                    # 011 -> 3 -> output = 010 = 2 -> n=3 -> n=2
                    # 010 -> 2
                else:
                    n+=1
            res+=1
        return res-1
"""
        if an odd number's bit rep does not contain a 2, then by subtracting by one the number is smaller (less divisions)
        and a power of two (5 = 101 -> 5-1 = 100 -> 010 -> 001)
        This only doesn't apply for 3 since adding is 2 steps and subtracting is only one step
        3 -> 2 -> 1 OR 3 -> 4 -> 2 -> 1
        EX.  

            n = 17 = 10001

            n&2 = 10001   output = 0 = 0
                    010

            n -= 1
            17 -> 16 -> 8 -> 4 -> 2 -> 1 = 5 steps

            if n += 1
            19 -> 18 -> 9 ->  -> 4 -> 2 -> 1
"""