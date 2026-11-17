class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        ans = [[1]]

        for row in range(1, numRows):
            length = row + 1

            row_create = [0 for i in range(length)]

            for i in range(len(row_create)):
                left = ans[row - 1][row - 1] #if i != 0 else 0
                right = ans[row - 1][row + 1] if i > len(row_create) else 0
                # print(f"{left} , {right}")
                row_create[i] = left + right
                print(row_create)


            

            ans.append(row_create)

            
        
        return ans 
        