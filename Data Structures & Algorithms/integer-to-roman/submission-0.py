class Solution:
    def intToRoman(self, num: int) -> str:
        mapping1 = {1000: 'M', 900: 'CM',500:'D', 400: 'CD', 100:'C', 90: 'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4: 'IV', 1:'I'}
        #we are gonna mod by the num div by the next largest value every time and append that many of that symbol to the res, then mod by that number
        res = ""
        for item in mapping1:
            numTimes = num // item

            while numTimes:
                res += (mapping1[item])
                numTimes -= 1
            num = num % item
            if not num:
                break
        return res
        