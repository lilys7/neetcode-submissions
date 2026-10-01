class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #append elt to stack, if the next elt(s) are greater then we pop off the stack and the val at that index as set length of stack 
        #iterate backwards?

        stack = [] #store indeces instead in the stack
        res = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1,-1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            
            if stack:
                res[i] = stack[-1] - i
            
            stack.append(i)
        return res

