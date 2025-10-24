from itertools import permutations

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        numbers = {1: ["1", "22"],
                   2: ["22", "122"],
                   3: ["122", "333", "1333"],
                   4: ["1333", "4444", "14444"],
                   5: ["14444", "22333", "55555", "122333"],
                   6: ["333221", "555551", "444422", "666666","1224444"],
                   }
        lookup = numbers[len(str(n))][:-1]
        choices = set()
        for i in lookup:
            choices.update(set(permutations(i)))
        choices = sorted(choices)
        for choice in choices:
            if n < int("".join(choice)):
                return int("".join(choice))
        return int(numbers[len(str(n))][-1])
        # for i in lookup:
        #     if n < int(i):
        #         choices = sorted(permutations(i))
        #         for choice in choices:
        #             if n < int("".join(choice)):
        #                 return int("".join(choice))
        return -1

print(Solution().nextBeautifulNumber(3000))