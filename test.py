n = int(raw_input())
ar = map(int, raw_input().strip().split())
ar.sort(reverse=True)
count = 0
max_num = max(ar)
print  ar.count(max(ar))
for i in range(0,len(ar)):
	if ar[i] == max_num:
		count +=1
	else:
		break
print count