class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # we are just passing this hash to avoid any errors 

        for s in strs:
            count = [0] * 26 
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s) #add all s to this count 
        return list(res.values())

        


        
        

