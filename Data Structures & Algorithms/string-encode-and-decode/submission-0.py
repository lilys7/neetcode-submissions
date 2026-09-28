class Solution:

    def encode(self, strs: List[str]) -> str:
        #append the length of the string + a # and then the rest of the string so we know how many letters to get
        output = []
        for s in strs:
            output.append(str(len(s)))
            output.append("#")
            output.append(s)
        print("".join(output))
        return "".join(output)

    def decode(self, s: str) -> List[str]:
        #read the length and loop up until that length
        #always gonna be number, #, string
        # 5#Hello5#World
        point = 0
        
        res = []
        while point < len(s):
            num = ""
            while s[point] != '#':
                num += (s[point])
                point += 1
            print("Number:", num)
            number = int(num)
            word = ""
            point += 1 #skip the #
            for i in range(number):
                word += (s[point])
                point += 1
            res.append(word)
            print("loop done")
        return res

        


