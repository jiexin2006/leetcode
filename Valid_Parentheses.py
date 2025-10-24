class Solution:
    def isValid(self, s: str) -> bool:
        store = []
        parentheses = {")": "(", "]":"[", "}":"{"}
        for i in range(len(s)):
            if s[i] in parentheses.values():
                store.append(s[i])
            else:
                if store[-1] == parentheses[s[i]]:
                    store.pop(-1)
                else:
                    return False

        return True if len(store)==0 else False







        # if len(s) % 2 == 1:
        #     return False
        # brackets = {
        #     "()": -1,
        #     "[]": -1,
        #     "{}": -1
        # }
        # positions = {
        #     "(" : "()",
        #     ")" : "()",
        #     "[" : "[]",
        #     "]" : "[]",
        #     "{" : "{}",
        #     "}" : "{}"
        # }
        # L = 0
        # R = len(s) - 1
        # while L < R:
        #     print(f"Now checking {L}: {s[L]} and {R}: {s[R]}")
        #     print(f"L: {brackets[positions[s[L]]]}, R: {brackets[positions[s[R]]]}")
        #     if brackets[positions[s[L]]] == -1:
        #         brackets[s[L]] = L
        #     else:
        #         if (abs(L - brackets[positions[s[L]]])+ 1) % 2 == 1:
        #             return False
        #         else:
        #             brackets[positions[s[L]]] = -1
        #     if brackets[positions[s[R]]] == -1:
        #         brackets[positions[s[R]]] = R
        #     else:
        #         if (abs(R - brackets[positions[s[R]]]) + 1) % 2 == 1:
        #             return False
        #         else:
        #             brackets[positions[s[R]]] = -1
        #     print(f"L: {brackets[positions[s[L]]]}, R: {brackets[positions[s[R]]]}")
        #
        #     L += 1
        #     R -= 1
        #
        #
        # print(brackets)
        # for k in brackets:
        #     if brackets[k] != -1:
        #         return False
        #
        # return True

print(Solution().isValid("()"))

