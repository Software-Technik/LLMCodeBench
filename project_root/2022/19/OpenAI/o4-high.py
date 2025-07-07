import sys,re
from math import prod
def parse_data(data):
    bps=[]
    for line in data:
        n=list(map(int,re.findall(r'\d+',line)))
        ore,clay,obs_ore,obs_clay,geo_ore,geo_obs=n[1:]
        bps.append(((ore,0,0,0),(clay,0,0,0),(obs_ore,obs_clay,0,0),(geo_ore,0,geo_obs,0)))
    return bps
def run_blueprints(bps,time):
    res=[]
    for bp in bps:
        cost_o,cost_c,cost_ob,cost_g=bp
        max_o=max(cost_o[0],cost_c[0],cost_ob[0],cost_g[0])
        max_c=cost_ob[1]
        max_ob=cost_g[2]
        best=0
        def dfs(t,ore,clay,obs,geo,ore_b,clay_b,obs_b,geo_b):
            nonlocal best
            best=max(best,geo+geo_b*t)
            if t==0 or geo+geo_b*t+t*(t-1)//2<=best:
                return
            if ore_b and obs_b:
                wo=(cost_g[0]-ore+ore_b-1)//ore_b if ore<cost_g[0] else 0
                wo2=(cost_g[2]-obs+obs_b-1)//obs_b if obs<cost_g[2] else 0
                w=wo if wo>wo2 else wo2
                if t>w:
                    dfs(t-w-1,ore+ore_b*(w+1)-cost_g[0],clay+clay_b*(w+1)-cost_g[1],obs+obs_b*(w+1)-cost_g[2],geo+geo_b*(w+1)-cost_g[3],ore_b,clay_b,obs_b,geo_b+1)
                    return
            if ore_b and clay_b and obs_b<max_ob:
                wo=(cost_ob[0]-ore+ore_b-1)//ore_b if ore<cost_ob[0] else 0
                wc=(cost_ob[1]-clay+clay_b-1)//clay_b if clay<cost_ob[1] else 0
                w=wc if wc>wo else wo
                if t>w:
                    dfs(t-w-1,ore+ore_b*(w+1)-cost_ob[0],clay+clay_b*(w+1)-cost_ob[1],obs+obs_b*(w+1)-cost_ob[2],geo+geo_b*(w+1)-cost_ob[3],ore_b,clay_b,obs_b+1,geo_b)
            if clay_b<max_c:
                wo=(cost_c[0]-ore+ore_b-1)//ore_b if ore<cost_c[0] else 0
                if t>wo:
                    dfs(t-wo-1,ore+ore_b*(wo+1)-cost_c[0],clay+clay_b*(wo+1)-cost_c[1],obs+obs_b*(wo+1)-cost_c[2],geo+geo_b*(wo+1)-cost_c[3],ore_b,clay_b+1,obs_b,geo_b)
            if ore_b<max_o:
                wo=(cost_o[0]-ore+ore_b-1)//ore_b if ore<cost_o[0] else 0
                if t>wo:
                    dfs(t-wo-1,ore+ore_b*(wo+1)-cost_o[0],clay+clay_b*(wo+1)-cost_o[1],obs+obs_b*(wo+1)-cost_o[2],geo+geo_b*(wo+1)-cost_o[3],ore_b+1,clay_b,obs_b,geo_b)
        dfs(time,0,0,0,0,1,0,0,0)
        res.append(best)
    return res
def part1(data):
    return sum((i+1)*v for i,v in enumerate(run_blueprints(parse_data(data),24)))
def part2(data):
    return prod(run_blueprints(parse_data(data)[:3],32))
data=[l.strip() for l in open(sys.argv[1])]
print(part1(data))
print(part2(data))