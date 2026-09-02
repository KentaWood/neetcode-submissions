class Solution:
    def calPoints(self, operations: List[str]) -> int:

        records = [] 


        for op in operations:
            
            print(f"{records}")

            if op.isdigit() or op[0] =="-":
                records.append(int(op))
            elif op == "+":
                records.append( records[-1] + records[-2])
            elif op == "D":
                records.append( records[-1] * 2)
            elif op == "C":
                records.pop()
                
        
        return sum(records) 
        