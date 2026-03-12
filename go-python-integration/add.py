import sys

def main():
    if len(sys.argv) != 3:
        print("Error: Two numbers required")
        sys.exit(1)

    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        print(a + b)   # Only prints the result (important for Go)
    except ValueError:
        print("Error: Invalid numbers")
        sys.exit(1)

if __name__ == "__main__":
    main()