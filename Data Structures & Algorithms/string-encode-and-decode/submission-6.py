class Solution:

    def encode(self, strs: List[str]) -> str:
        coded = ""

        for word in strs:
            coded += str(len(word)) + "#" + word

        return coded



    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while(i < len(s)): 
            j = i

            #increment j until j is #, end of length seq
            while s[j] != "#":
                j += 1
            
            #now j = #, exlcusive of j
            length = int(s[i:j])

            # i is start of word, j is the end of the said word 
            i = j + 1 
            j = j + length + 1

            decoded.append(s[i:j])

            i = j


        return decoded



