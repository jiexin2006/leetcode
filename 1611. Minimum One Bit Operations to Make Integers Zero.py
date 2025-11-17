def recursive(num, operations, k):
    print("Checking: for num=", num, " ", operations[2 ** k], "- recursive(", num - 2 ** k, ", operations, ", k)
    if num == 2**k or num ==1:
        return operations[num]
    else:
        temp = k
        temp-=1
        while 2**temp > num-2**k:
            temp -=1
        print("num-2**k = ", num-2**k, ",temp = ", temp)
        return operations[2**k] - recursive(num-2**k, operations, temp)


class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        k = 1
        operations = {1:1}
        while 2**k <= n:
            operations[2**k] = 2*operations[2**(k - 1)]+1
            k += 1
        print(operations)
        return recursive(n, operations, k-1)

print(Solution().minimumOneBitOperations(16))