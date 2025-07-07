import sys

FIVE_OF_A_KIND = 7
FOUR_OF_A_KIND = 6
FULL_HOUSE = 5
THREE_OF_A_KIND = 4
TWO_PAIR = 3
ONE_PAIR = 2
HIGH_CARD = 1

CARDS = {"A":14,"K":13,"Q":12,"J":11,"T":10,"9":9,"8":8,"7":7,"6":6,"5":5,"4":4,"3":3,"2":2}

def get_hand_type(vals):
    freq={}
    for v in vals: freq[v]=freq.get(v,0)+1
    counts=sorted(freq.values(),reverse=True)
    l=len(freq)
    m=counts[0]
    if l==1: return FIVE_OF_A_KIND
    if l==2:
        if m==4: return FOUR_OF_A_KIND
        return FULL_HOUSE
    if l==3:
        if m==3: return THREE_OF_A_KIND
        return TWO_PAIR
    if l==4: return ONE_PAIR
    return HIGH_CARD

with open(sys.argv[1]) as f:
    hs=[]
    for line in f:
        h,s=line.split()
        vals=[CARDS[c] for c in h]
        ht=get_hand_type(vals)
        hs.append(((ht,)+tuple(vals),int(s)))
hs.sort(key=lambda x:x[0])
res=sum((i+1)*score for i,(k,score) in enumerate(hs))
sys.stdout.write(f"{res} {res}")