class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        ans = strs[0]

        # for word in strs[1:]: <-- recreates the list

        for i in range(1, len(strs)):

            word = strs[i]
            
            p = 0
            
            
            while p < len(word) and p < len(ans):
                if word[p] != ans[p]:
                    break
                
                p += 1
            
            print(ans, p)

            ans = ans[:p]

                    
        return ans

