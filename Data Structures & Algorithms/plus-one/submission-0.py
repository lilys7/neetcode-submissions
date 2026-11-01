class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = ""
        for num in digits:
            res += str(num)
        total = str(int(res) + 1)
        resList = []
        for s in total:
            resList.append(int(s))
        return resList
    