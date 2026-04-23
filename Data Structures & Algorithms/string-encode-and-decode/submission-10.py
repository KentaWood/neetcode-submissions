class Solution:

    def encode(self, strs: List[str]) -> str:
        
        coded = ""

        for s in strs:
            length = len(s)
            coded += str(length) + "#" + s
        
        return coded


    def decode(self, s: str) -> List[str]:

        res = []

        l = 0
        r = 0
        while r < len(s):
            l = r 

            while s[r] != "#":
                r += 1
            
            length = int(s[l:r])
            l = r + 1
            r = r + length

            res.append(s[l:r + 1])

            r += 1
        
        return res

