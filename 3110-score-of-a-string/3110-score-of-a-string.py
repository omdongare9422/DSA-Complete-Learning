class Solution:
    def scoreOfString(self, s: str) -> int:
        c=0
        i=1
        while i<len(s):
            c+=abs(ord(s[i-1])-ord(s[i]))
            i+=1

        return c 