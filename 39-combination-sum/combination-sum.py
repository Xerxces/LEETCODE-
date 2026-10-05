class Solution:
    def combinationSum(
        self, candidates: list[int], target: int
    ) -> list[list[int]]:
        candidates.sort()
        res = []
        def backtrack(start: int, remaining: int, path: list[int]):
            if remaining == 0:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break
                path.append(candidates[i])
                backtrack(i, remaining - candidates[i], path)
                path.pop()
        backtrack(0, target, [])
        return res