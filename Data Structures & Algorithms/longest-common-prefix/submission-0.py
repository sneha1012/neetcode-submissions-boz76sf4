class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #we need to check if inbound, go or check all of them simulatenouly
        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res #zeroth string in strs, and then index i in that string 
            
            res += strs[0][i] #add these charcters too if we find similar stuff
        return res 
