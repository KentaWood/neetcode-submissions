class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""

        for word in strs:
            length = str(len(word))
            res += length + "#" + word

        return res

    def decode(self, s: str) -> List[str]:
        res = []

        l,r = 0,0
        # print('3e32')

        while r < len(s):
            # print(r,res)
            l = r 
            # print("DSDD")

            while s[r] != "#":
                r += 1
            print(s)    
            print(l,r)
            length = int(s[l:r])
            l = r + 1

            for _ in range(length + 1):
                r += 1
            
            res.append(s[l:r])
            


        return res
