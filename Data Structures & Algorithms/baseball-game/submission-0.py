class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        our_array = []

        for i in range(len(operations)):
            if operations[i] == "+":
                our_array.append(our_array[-1] + our_array[-2])
            elif operations[i] == "C":
                our_array.pop()
            elif operations[i] == "D":
                our_array.append(our_array[-1]*2)

            else:
                our_array.append(int(operations[i]))

        return (sum(our_array))
