class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        first = len(s) % k
        parts = []

        if first:
            parts.append(s[:first])

        for i in range(first, len(s), k):
            parts.append(s[i:i + k])

        return "-".join(parts)