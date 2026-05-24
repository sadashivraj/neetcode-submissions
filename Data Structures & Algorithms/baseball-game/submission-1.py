class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = 0
        stack = []

        for i in range(len(operations)):
            try:
                val = int(operations[i])
            except ValueError as e:
                val = None
            if isinstance(val, int):
                stack.append(val)
                score += val
            elif operations[i] == '+':
                val = stack[-1]+stack[-2]
                stack.append(val)
                score += val
            elif operations[i] == 'D':
                val = stack[-1]*2
                stack.append(val)
                score += val
            elif operations[i] == 'C':
                score -= stack[-1]
                stack.pop()
                

        return score

        