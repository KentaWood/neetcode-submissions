class Solution:

    def encode(self, strs: List[str]) -> str:
        
        ans = ""

        for word in strs:
            ans += str(len(word)) + '#' + word

        print(ans)

        return ans



    def decode(self, s: str) -> List[str]:

        ans = []

        r = 0

        while r > len(s):
            l = r

            # we start @ the beginning of the length of the coded strings
            while r[s] != "#":
                r += 1
            #r is at the # signaling the end of length of the coded word
            length = int(s[l:r])

            l = r + 1
            r = r + length + 1 
            print(l, r)






        return []
