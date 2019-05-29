def main():
    T = int(input())

    for i in range(T):
        rc = input()
        phases = list(map(int, input().split()))
        states = list(map(int, input().split()))

        c = len(states)
        matrixScore = []

        for ri in phases:
            matrixScore.append(float(ri)/c)

        finalScore = sum(matrixScore)*c

        if(finalScore == sum(states)):
            print("YES")
        else:
            print("NO")


main()
