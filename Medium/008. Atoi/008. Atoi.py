class Solution:
    def myAtoi(self, s: str) -> int:
        MAX = 2**31
        nums = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
        res = sign = 0
        first_num = -1
        for i in range(len(s)):
            # if not a num
            if s[i] not in nums:
                # if first num alr passed
                if first_num != -1:
                    break
                else:
                    if s[i] == ' ' and sign == 0:
                        continue
                    elif sign == 0 and (s[i] == '+' or s[i] == '-'):
                        sign = 1 if s[i] == '+' else -1
                    else:
                        break
            else:
                res *= 10
                if first_num == -1:
                    first_num = i
                res += ord(s[i]) - ord('0')

        res *= sign if sign != 0 else 1
        if res < -1*MAX:
            return -1 * MAX
        if res > MAX-1:
            return MAX-1

        return res


            
                


        