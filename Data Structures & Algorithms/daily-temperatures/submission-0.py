class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):

            while stack:
                top_index, top_temp = stack[-1]

                if temp > top_temp:
                    stack.pop()
                    result[top_index] = i - top_index
                else:
                    break

            stack.append((i, temp))

        return result