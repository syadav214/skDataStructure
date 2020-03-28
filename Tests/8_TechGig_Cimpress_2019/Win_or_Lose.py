def main():
    T = int(input())

    strength = [0 for i in range(T)]
    energy = [0 for i in range(T)]

    for i in range(T):
        N = int(input())
        strength[i] = list(map(int, input().split()))
        energy[i] = list(map(int, input().split()))

    for i in range(T):
        strength[i].sort()
        energy[i].sort()
        flag = 0
        result = "WIN"
        for j in range(len(energy[i])):
            if energy[i][j] < strength[i][j]:
                result = "LOSE"
                break
        print(result)


main()
