class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def parseBoolRecur(i, op):
            # keep count of truth values
            # index: 0 = false, 1 = true
            t_values = [0, 0]

            operations = set(('!', '&', '|'))

            # while within cur parentheses
            while expression[i] != ')':
                if expression[i] == 'f':
                    t_values[0] += 1

                elif expression[i] == 't':
                    t_values[1] += 1

                elif expression[i] in operations:
                    val, i = parseBoolRecur(i+2, expression[i])
                    if val == True:
                        t_values[1] += 1
                    else:
                        t_values[0] += 1
                        
                i += 1

            # apply relevant operation
            if op == '!':
                t_values[0], t_values[1] = t_values[1], t_values[0]
            
            elif op == '|':
                if t_values[1] > 0:
                    t_values[0] = 0
            
            elif op == '&':
                if t_values[0] > 0:
                    t_values[1] = 0

            return (False if t_values[1] == 0 else True, i)

        # +2 to skip over paren and operation
        res, index = parseBoolRecur(2, expression[0])
        return res

        """
        Time Complexity = O(n) (since i'm starting where i left off, it's just one pass)
        Space Complexity = O(?), ? = number of operators in th expression (should be O(n) then, but idk)
        """

