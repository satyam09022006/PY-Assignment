def max_leftover_cakes(N):
    max_leftover = 0
    optimal_package_size = N

    for A in range(N - 1, 0, -1):
        leftover = N % A
        if leftover > max_leftover:
            max_leftover = leftover
            optimal_package_size = A
        if max_leftover > N - A:
            break

    return optimal_package_size

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(max_leftover_cakes(N))

if __name__ == "__main__":
    main()