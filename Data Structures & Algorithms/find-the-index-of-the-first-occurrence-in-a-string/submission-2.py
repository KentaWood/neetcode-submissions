class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        for i in range(len(haystack)):
            
            p = 0
            if haystack[i] == needle[p]:
                
                print(haystack[i + p], needle[p])

                while i + p < len(haystack) and p < len(needle)  and haystack[i + p] == needle[p]:
                    p += 1  

                    if haystack[i:i +p] == needle:
                        return i 
                
                

        
        return -1 
            

        