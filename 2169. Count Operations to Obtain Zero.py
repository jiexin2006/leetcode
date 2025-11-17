class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0
        while num1 != 0 and num2 != 0:
            if num1>num2:
                num1 = abs(num1-num2)
            else:
                num2 = abs(num1-num2)
            count += 1
            # print("num1:", num1,"num2:",  num2)
        return count

print(Solution().countOperations(10,10))

# if num1 == 0 or num2 == 0:
#     return 0
# elif num1 < num2:
#     return self.countOperations(num2, num1)
# else:
#     return num1 // num2 + self.countOperations(num2, num1 % num2)