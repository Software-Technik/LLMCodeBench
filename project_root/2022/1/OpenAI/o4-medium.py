import sys
first=second=third=0
curr=0
with open(sys.argv[1]) as f:
    for line in f:
        line=line.strip()
        if line:
            curr+=int(line)
        else:
            if curr>first:
                third,second,first=second,first,curr
            elif curr>second:
                third,second=second,curr
            elif curr>third:
                third=curr
            curr=0
if curr>first:
    third,second,first=second,first,curr
elif curr>second:
    third,second=second,curr
elif curr>third:
    third=curr
sys.stdout.write(f"{first}\n{first+second+third}\n")