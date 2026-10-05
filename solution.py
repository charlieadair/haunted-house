from pathlib import Path

def main():
    print("Hello, World!")
    for tests in 'test1', 'test2', 'test3':
        runTest(tests)

def runTest(file_path: str | Path) -> bool:
    with open(file_path, "r") as f:

        # Parse parameters n and k
        params = f.read().strip().split()
        n = params[0]
        k = params[1]
        print(f"n: {n}, k: {k}")

        

        

if __name__ == "__main__":
    main()