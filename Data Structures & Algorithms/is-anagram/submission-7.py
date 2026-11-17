class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        
        # n log n time 1 space 
        return sorted(s) == sorted(t)




        # 2. N time 26 -> constant space 

        # if len(s) != len(t): return False 

        # s_count, t_count = [0] * 26, [0] * 26
        # # print(s_count, t_count)

        # for i in range(len(s)):
            
        #     s_count[ord(s[i]) - ord('a')] += 1
        #     t_count[ord(t[i]) - ord('a')] += 1

        # print(tuple(s_count), (t_count))

        # return tuple(s_count) == tuple(t_count)



        # 1. N time N space
        # return Counter(s) == Counter(t)

        