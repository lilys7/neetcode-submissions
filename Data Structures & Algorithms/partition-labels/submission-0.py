class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #counter, iterate through the list and decrement the val found every time. any time we hit a 0 for all seen, we can take that substring out
        counts = Counter(s)
        res = []
        seen = set()
        newString = ""
        for ch in s:
            seen.add(ch)
            counts[ch] -= 1
            if counts[ch] == 0:
                seen.remove(ch)
                if seen:
                    newString += ch
                else:
                    res.append(1 + len(newString))
                    newString = ""
            else:
                newString += ch
        return res

