# python3
# Kristaps Arnolds Kaidalovs 16.grupa 201RDK001

def swap(data, i, j):
    t = data[0][i]
    data[0][i] = data[0][j]
    data[0][j] = t
    data[1].append((i, j))

def heapify(data, n, i):
    next = i
    nums = data[0]

    while True:
        if 2*i+1 < n and nums[2*i+1] < nums[next]:
            next = 2*i+1

        if 2*i+2 < n and nums[2*i+2] < nums[next]:
            next = 2*i+2

        if i == next: break
        else:
            swap(data, i, next)
            i = next

def build_heap(data):
    n = len(data[0])
    
    for i in range(n//2, -1, -1):
        heapify(data, n, i)

def input_data():
    input_type = input().strip()
    if (input_type.upper() == "F"):
        # input file name to use, prepend "tests/" due to inaccurate input
        file = open("tests/" + input())
        # input number of elements
        count = int(file.readline())
        # input values separated with spaces, split these values in an array
        data = (list(map(int, file.readline().split())), [])
    elif (input_type.upper() == "I"):
        # input number of elements
        count = int(input())
        # input values separated with spaces, split these values in an array
        data = (list(map(int, input().split())), [])
    else:
        raise RuntimeError(f"Invalid input type ({input_type})")

    # checks if length of data is the same as the said length
    if len(data[0]) != count:
        raise RuntimeError("Mismatching input length"
                          f" (got {count}, expected, {len(data[0])})")

    return data

def main():
    # input data
    data = input_data()

    # builds min heap and list of requried swaps
    build_heap(data)

    # output all swaps
    print(len(data[1]))
    for i, j in data[1]:
        print(i, j)

if __name__ == "__main__":
    main()
