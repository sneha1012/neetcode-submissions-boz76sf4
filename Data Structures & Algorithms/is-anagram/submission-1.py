class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #we can use hashmaps and and match these hashes 
        countT, countS = {}, {} #value:count

        if len(s) != len(t): #maps 
            return False 
        
        for i in range(len(s)):
            countS[s[i]] = 1+ countS.get(s[i], 0)
            countT[t[i]] = 1+ countT.get(t[i], 0)
        return countS == countT

        
        