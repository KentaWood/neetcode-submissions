class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()

        def bt(perm: List[int], idx: int, total: int) -> None:

            if total == target:
                res.append(perm[:])
                return
            
            if idx >= len(candidates) or total > target:
                return
            
            perm.append(candidates[idx])
            bt(perm,idx + 1, total + candidates[idx])
            perm.pop()

            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
                idx += 1 

            bt(perm,idx + 1, total )


        bt([],0,0)

        return res