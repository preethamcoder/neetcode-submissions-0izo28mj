import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = frozenset(['+', '-', "*", "/"])
        nums = []
        res = 0
        for each in tokens:
            print(nums)
            if each not in operators:
                nums.append(int(each))
            else:
                first = nums.pop()
                second = nums.pop()
                if each == '+':
                    nums.append(first+second)
                elif each == '-':
                    nums.append(second-first)
                elif each == '*':
                    nums.append(first*second)
                else:
                    res = second/first
                    if res < 0:
                        nums.append(math.ceil(res))
                    else:
                        nums.append(math.floor(res))
        return nums.pop()