class Solution:
    def encode(self, words:List[str]) -> str:
        coded = ""
        for word in words:
            # print(str(len(word)) + "#" + word)
            coded += str(len(word)) + "#" + word
        
        return coded  
            
    def decode(self, word:str) -> List[str]:
        i = 0
        decoded = []
        
        while i < len(word):
            j=i
            
            while word[j] != "#":
                j+= 1

            word_length = int(word[i:j])
            
            decoded.append(word[j+1: j +  word_length + 1])
            
            i = j + 1 + word_length 
            
            
            
            
        
        
        return decoded