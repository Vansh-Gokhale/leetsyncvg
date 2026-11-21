class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        i = 0
        n = len(words)

        while i < n:
            j = i
            line_length = 0

            while j < n and line_length + len(words[j]) + (j - i) <= maxWidth:
                line_length += len(words[j])
                j += 1

            count = j - i
            spaces = maxWidth - line_length

            if j == n or count == 1:
                line = ' '.join(words[i:j])
                result.append(line + ' ' * (maxWidth - len(line)))
            else:
                gaps = count - 1
                space, extra = divmod(spaces, gaps)
                line = ''

                for k in range(i, j - 1):
                    line += words[k] + ' ' * (space + (1 if k - i < extra else 0))

                line += words[j - 1]
                result.append(line)

            i = j

        return result