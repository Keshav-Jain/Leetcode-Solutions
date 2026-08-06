class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts={}
        if len(s)!=len(t):
            return False

        for i in range(0,len(s)):
                counts[s[i]] = counts.get(s[i],0)+1
                counts[t[i]] = counts.get(t[i],0)-1
        for count in counts.values():
                if count!=0:
                    return False
        return True