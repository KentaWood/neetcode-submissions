class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []
        mapping = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
            }

        ans = []

        def bt(curr: str, combo: str) -> None:
            print("here")
    
            if len(combo) == len(digits):
                
                
                ans.append(combo)
                return

            p = len(curr)
            # print(f"curr: {curr}  pointer: {p}")
            
            for let in mapping[digits[p]]:
                # print(curr + digits[p], combo + let)
                bt(curr + digits[p], combo + let)
                
            
            

        bt("","")

        return ans

        