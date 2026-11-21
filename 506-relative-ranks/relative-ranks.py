class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ranks = [""] * len(score)

        for rank, (index, _) in enumerate(sorted(enumerate(score), key=lambda x: -x[1])):
            ranks[index] = (
                "Gold Medal" if rank == 0 else
                "Silver Medal" if rank == 1 else
                "Bronze Medal" if rank == 2 else
                str(rank + 1)
            )

        return ranks