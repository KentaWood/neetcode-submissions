class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        for word in strs:
            encoded_str += str(len(word)) + "*" + word

        print(encoded_str)
        return encoded_str

    def decode(self, s: str) -> List[str]:

        ans = []

        decoded = []
        l, r = 0, 0 
        print(s)
        while r < len(s):

            while r < len(s) and s[r] != "*":
                r += 1
            
            # r == "*"
            length = int(s[l:r])
            
            l, r = r + 1, r + length + 1
            
            print(l,r,length)

            ans.append(s[l:r])

            l, r = r, r + 1
            print(l,r,length)

            
        
        return ans




            





        return ["1"]
