class Solution:
    def isValid(self, s: str) -> bool:
        comp = {
            '}':'{',
            ']':'[',
            ')':'('
        }

        stack = []

        for c in s:
            if c in comp:
                if stack and stack[-1] == comp[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if not stack:
            return True
        else:
            return False