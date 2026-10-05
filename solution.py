from pathlib import Path
from collections.abc import Callable

def main():
    print("==> RECURSIVE SOLUTION")
    for test in 'test1', 'test2', 'test3':
        print(f"{test}: {'PASS' if runTest(test, recursiveSolution) else 'FAIL'}")
    print("==> DYNAMIC PROGRAMMING SOLUTION")
    for test in 'test1', 'test2', 'test3':
        print(f"{test}: {'PASS' if runTest(test, dpSolution) else 'FAIL'}")

def runTest(file_path: str | Path, solution: Callable[[int, int, list[list[int]]], int]
) -> bool:
    with open(file_path, "r") as f:

        # Parse parameters n and k
        params = f.readline().strip().split()
        n = int(params[0])
        k = int(params[1])

        rooms = list[list[int]]()
        for line in f:
            p = line.strip().split()
            if len(p) == 0: break
            rooms.append([int(x) for x in p])

        expected = int(f.read().strip().split()[0])
        actual = solution(n, k, rooms)

        return expected == actual
        

def recursiveSolution(n: int, k: int, rooms: list[list[int]]) -> int:
    def best(row: int, remaining: int, previous: str) -> int:

        if remaining == 0: return sum(left + right for left, right in rooms[row:])

        # Handles the case where there are more doors to close than remaining rows. IE not a solution.
        if remaining > n - row: return float('-inf')
    
        left, right = rooms[row]

        # keep both rooms open 
        answer = left + right + best(row + 1, remaining, "neither")

        # if previous door was left -> you can calculate the maximum if you chose right, and vice versa.
        # if previous was neither -> calculate the maximum for both choices
        if previous != "left":
            answer = max(answer, left + best(row + 1, remaining - 1, "right"))
        if previous != "right":
            answer = max(answer, right + best(row + 1, remaining - 1, "left"))

        return answer

    return best(0, k, "neither")

def dpSolution(n: int, k: int, rooms: list[list[int]]) -> int:

    NEITHER, LEFT, RIGHT = 0, 1, 2

    # init a 3D array — dp[row][remaining doors to close][previous choice (neither/left/right)].
    # Assume all entries are invalid solutions at first (-inf)
    dp = [[[float("-inf")]   * 3 for _ in range(k + 1)]   for _ in range(n + 1)]

    for previous in range(3):
        dp[n][0][previous] = 0

    for row in range(n - 1, -1, -1):

        for previous in range(3):

            left, right = rooms[row]

            for remaining in range(k + 1):
                # keep both rooms open 
                answer = left + right + dp[row + 1][remaining][NEITHER]
                if remaining > 0:

                    # if previous door was left -> you can calculate the maximum if you chose right, and vice versa.
                    # if previous was neither -> calculate the maximum for both choices
                    if previous != LEFT:
                        answer = max(answer, left + dp[row + 1][remaining - 1][RIGHT])
                    if previous != RIGHT:
                        answer = max(answer, right + dp[row + 1][remaining - 1][LEFT])

                dp[row][remaining][previous] = answer

    return dp[0][k][NEITHER]


if __name__ == "__main__":
    main()