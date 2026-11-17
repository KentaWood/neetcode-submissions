class Solution:
    def calPoints(self, operations: List[str]) -> int:

        records = [] 
        

        for op in operations:

            if op.isdigit():
                records.append(int(op))
            elif op == "+":
                records.append( records[-1] + records[-2])
            elif op == "D":
                records.append( records[-1] * 2)
            else:
                records.pop()
                
            print(f"{records}")
        
        return sum(records) 
        