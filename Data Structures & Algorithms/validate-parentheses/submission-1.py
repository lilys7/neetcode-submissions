class Solution:
    def isValid(self, s: str) -> bool:
        #use a stack as that is lifo
        closing = { ')' : '(', ']' : '[', '}':'{'}
        res = []
        #if odd, automatically not correct
        if len(s) % 2 != 0:
            return False
        
        for c in s:
            if c in closing:
                if not res:
                    return False
                last = res.pop()
                if last != closing[c]:
                    return False
            else:
                res.append(c)
        return res == []


