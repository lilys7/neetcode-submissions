class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #make array of alphabetical values 26 total to see how many of each char there is
        #iterate through all elements every time to see if the alphabetical list made from that word is the same. if yes, append that word to the list and keep going. clear alphabetical list after
        sortedStrs = defaultdict(list)
        for str in strs:
            s = "".join(sorted(str))
            sortedStrs[s].append(str)
        return list(sortedStrs.values())

