import sys,re
from array import array
def run_game(players,last_marble):
    size=last_marble+1
    nxt=array('I',[0])*size
    prv=array('I',[0])*size
    nxt[0]=prv[0]=0
    current=0
    scores=[0]*players
    for m in range(1,last_marble):
        p=m%players
        if m%23:
            one=nxt[current]
            two=nxt[one]
            nxt[one]=m; prv[m]=one
            nxt[m]=two; prv[two]=m
            current=m
        else:
            scores[p]+=m
            cur=current
            for _ in range(7): cur=prv[cur]
            scores[p]+=cur
            left=prv[cur]; right=nxt[cur]
            nxt[left]=right; prv[right]=left
            current=right
    return max(scores)
with open(sys.argv[1]) as f:
    players,last=map(int,re.findall(r'\d+',f.readline()))
sys.stdout.write(f"{run_game(players,last)} {run_game(players,last*100)}")