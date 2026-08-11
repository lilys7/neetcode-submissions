class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = defaultdict(list)
        values = {}
        for s in strs:
            chars = [0] * 26
            for ch in s:
                
                chars[ord(ch) - ord('a')] += 1
            ret[tuple(chars)].append(s)
        return list(ret.values())