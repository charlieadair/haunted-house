from pathlib import Path

def main():
    print("Hello, World!")
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
    return 0;



        

if __name__ == "__main__":
    main()