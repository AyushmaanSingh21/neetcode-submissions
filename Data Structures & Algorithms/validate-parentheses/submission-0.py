class Solution:
    def isValid(self, s: str) -> bool:
        # Map closing brackets to their matching opening brackets
        mapping = {")": "(", "}": "{", "]": "["}
        stack = []

        for i in s:
            # If it's a closing bracket
            if i in mapping:
                # Pop the top element if stack isn't empty, else use a dummy value
                top_element = stack.pop() if stack else '#'
                
                # Check if the opening bracket matches
                if mapping[i] != top_element:
                    return False
            else:
                # It's an opening bracket, push it onto the stack
                stack.append(i)

        # The string is valid only if the stack is completely empty
        return not stack

            
        