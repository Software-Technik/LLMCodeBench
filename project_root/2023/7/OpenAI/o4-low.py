import sys
from collections import Counter

FIVE_OF_A_KIND=7;FOUR_OF_A_KIND=6;FULL_HOUSE=5;THREE_OF_A_KIND=4;TWO_PAIR=3;ONE_PAIR=2;HIGH_CARD=1
CARDS={"A":14,"K":13,"Q":12,"J":11,"T":10,"9":9,"8":8,"7":7,"6":6,"5":5,"4":4,"3":3,"2":2}

def get_hand_type(hand):
    c=Counter(hand)
    l=len(c)
    if l==1: return FIVE_OF_A_KIND
    if l==2:
        m=c.most_common(1)[0][1]
        if m==4: return FOUR_OF_A_KIND
        return FULL_HOUSE
    if l==3:
        m=c.most_common(1)[0][1]
        return THREE_OF_A_KIND if m==3 else TWO_PAIR
    if l==4: return ONE_PAIR
    return HIGH_CARD

def score(text):
    lines=text.splitlines()
    data=[]
    for line in lines:
        h,s=line.split()
        t=get_hand_type(h)
        v=tuple(CARDS[c] for c in h)
        data.append((t,v,int(s)))
    data.sort(key=lambda x:(x[0],x[1]))
    total=0
    for i,(_,_,s) in enumerate(data,1):
        total+=i*s
    return total

with open(sys.argv[1]) as f:
    txt=f.read()
print(score(txt),score(txt))