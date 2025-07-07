import sys
data = open(sys.argv[1],'rb').read().strip()
n = len(data)
half = n//2
r1 = r2 = 0
for i in range(n):
    b = data[i]
    if b == data[(i+1)%n]:
        r1 += b-48
    if b == data[(i+half)%n]:
        r2 += b-48
print(r1)
print(r2)