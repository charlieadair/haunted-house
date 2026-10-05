from pathlib import Path
from unittest import case
from unittest import case
from xmlrpc.client import MAXINT

def main():
    for tests in 'test1', 'test2', 'test3':
        print(f"{tests}: {'PASS' if runTest(tests) else 'FAIL'}")

def runTest(file_path: str | Path) -> bool:
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
        actual = solution(n, k, rooms);

        return expected == actual;
        

def solution(n: int, k: int, rooms: list[list[int]]) -> int:
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
        

if __name__ == "__main__":
    main()