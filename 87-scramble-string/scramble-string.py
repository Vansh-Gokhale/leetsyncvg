class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        from functools import lru_cache
        from collections import Counter

        if len(s1) != len(s2) or Counter(s1) != Counter(s2):
            return False

        @lru_cache(None)
        def dp(a, b, n):
            if s1[a:a+n] == s2[b:b+n]:
                return True

            if Counter(s1[a:a+n]) != Counter(s2[b:b+n]):
                return False

            for i in range(1, n):
                if (dp(a, b, i) and dp(a+i, b+i, n-i)) or \
                   (dp(a, b+n-i, i) and dp(a+i, b, n-i)):
                    return True

            return False

        return dp(0, 0, len(s1))