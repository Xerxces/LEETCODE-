class Solution:
    def combinationSum2(
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
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i], path)
                path.pop()
        backtrack(0, target, [])
        return res