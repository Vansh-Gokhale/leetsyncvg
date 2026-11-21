class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"

        for _ in range(n - 1):
            i = 0
            current = []

            while i < len(result):
                j = i
                while j < len(result) and result[j] == result[i]:
                    j += 1

                current.append(str(j - i))
                current.append(result[i])
                i = j

            result = ''.join(current)

        return result