def main():
    T = int(input())

    for i in range(T):
        rc = input()
        phases = list(map(int, input().split()))
        states = list(map(int, input().split()))

        c = len(states)
        matrixScore = []

        for ri in phases:
            tempArr = []
            mod = ri % c
            if(mod == 0):
                tempArr.extend([ri/c for i in range(c)])
            else:
                num = (ri - mod) / c
                tempArr.extend([num for i in range(c)])
                tempArr[len(tempArr)-1] = mod
            matrixScore.append(tempArr)

        result = 'YES'
        for i in range(c):
            getSum = 0
            for xyz in matrixScore:
                getSum += xyz[i]
            if(getSum != states[i]):
                result = 'NO'
                break

        print(result)


main()
