class Solution:
    def calPoints(self, operations: List[str]) -> int:

        # gonne bae treated as a stack
        records = []

        for op in operations:

            print(f"{records}")

            match op:

                case "+":
                    records.append(records[-1] + records[-2])

                case "D":
                    records.append(records[-1] * 2)

                case "C":

                    records.pop()

                case _:
                    records.append(int(op))
        



        return sum(records)