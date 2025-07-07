import sys
from array import array
def main():
    with open(sys.argv[1]) as f:
        A = int(f.read().strip())
    limit = A//10
    arr1 = array('I',[0])*(limit+1)
    for i in range(1,limit+1):
        for j in range(i,limit+1,i):
            arr1[j]+=i
    ans1=1
    for i in range(1,limit+1):
        if arr1[i]*10>=A:
            ans1=i
            break
    del arr1
    arr2 = array('I',[0])*(limit+1)
    for i in range(1,limit+1):
        m=i*50
        if m>limit: m=limit
        for j in range(i,m+1,i):
            arr2[j]+=i
    ans2=1
    for i in range(1,limit+1):
        if arr2[i]*11>=A:
            ans2=i
            break
    sys.stdout.write(f"{ans1}\n{ans2}\n")
if __name__=="__main__":
    main()