time = raw_input().strip()
h, m, s = map(str, time[:-2].split(':'))
h = int(h)
p = time[-2:]
h = h % 12 + (p.upper() == 'PM') * 12
ss = str(h).zfill(2)+":"+str(m)+":"+str(s)
print ss