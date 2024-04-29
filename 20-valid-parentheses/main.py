# Time: O(n)
# Space: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "(":
                # () => ex. 1
                stack.append(1)
            if char == "[":
                # [] => ex. 2
                stack.append(2)
            if char == "{":
                # {} => ex. 3
                stack.append(3)

            if char == ")":
                if not stack or stack.pop() != 1 :
                    return False
            if char == "]":
                if not stack or stack.pop() != 2:
                    return False
            if char == "}":
                if not stack or stack.pop() != 3:
                    return False
                
        return not stack
        