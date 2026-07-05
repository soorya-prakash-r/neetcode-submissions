class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for i in tokens:
            if i not in ["*", "/", "+", "-"]:
                stack.append(int(i))
            else:
                y = stack.pop()
                x = stack.pop()
                res = 0
                if i == "*":
                    res = x * y
                elif i == "-":
                    res = x - y
                elif i == "+":
                    res = x + y
                else:
                    res = int(x / y)
                stack.append(res)
                print(stack)

        return int(stack[-1])
        