class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empty = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty.append((i, j))
                else:
                    bit = 1 << (int(board[i][j]) - 1)
                    rows[i] |= bit
                    cols[j] |= bit
                    boxes[(i // 3) * 3 + j // 3] |= bit

        def backtrack(pos):
            if pos == len(empty):
                return True

            best = pos
            min_count = 10

            for k in range(pos, len(empty)):
                i, j = empty[k]
                box = (i // 3) * 3 + j // 3
                mask = 511 & ~(rows[i] | cols[j] | boxes[box])
                count = mask.bit_count()

                if count < min_count:
                    min_count = count
                    best = k

                if count == 1:
                    break

            if min_count == 0:
                return False

            empty[pos], empty[best] = empty[best], empty[pos]
            i, j = empty[pos]
            box = (i // 3) * 3 + j // 3
            mask = 511 & ~(rows[i] | cols[j] | boxes[box])

            while mask:
                bit = mask & -mask
                mask -= bit
                digit = str(bit.bit_length())

                board[i][j] = digit
                rows[i] |= bit
                cols[j] |= bit
                boxes[box] |= bit

                if backtrack(pos + 1):
                    return True

                rows[i] ^= bit
                cols[j] ^= bit
                boxes[box] ^= bit
                board[i][j] = '.'

            empty[pos], empty[best] = empty[best], empty[pos]
            return False

        backtrack(0)