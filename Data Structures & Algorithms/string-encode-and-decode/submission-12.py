class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        for word in strs:
            encoded_str += str(len(word)) + "*" + word

        print(encoded_str)
        return encoded_str

    def decode(self, s: str) -> List[str]:

        ans = []
        
        if s[0] == "0":
            return [""]

        decoded = []
        l, r = 0, 0 

        while r < len(s):

            while r < len(s) and s[r] != "*":
                r += 1
            
            # r == "*"
            length = int(s[l:r])
            
            l, r = r + 1, r + length
            print(l,r)
            ans.append(s[r + 1 :length + 1])


        
        return ans




            





        return ["1"]
