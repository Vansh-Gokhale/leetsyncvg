class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [
            set("qwertyuiop"),
            set("asdfghjkl"),
            set("zxcvbnm")
        ]

        return [
            word for word in words
            if any(set(word.lower()).issubset(row) for row in rows)
        ]