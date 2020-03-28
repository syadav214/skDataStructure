import math
def main():
    N = int(input())
    requiredQty = list(map(int, input().split()))
    presentQty = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        val = math.floor(presentQty[i]/requiredQty[i])
        if(i==0):
            ans = val
        if(ans > val):
            ans = val
    print(N, requiredQty,presentQty,ans)
main()

"""
4
2 5 6 3
20 40 90 50
Output: 8
Get the output from which minimum can be produced from each
"""