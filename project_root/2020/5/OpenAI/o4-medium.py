import sys
tr = str.maketrans({'F':'0','B':'1','L':'0','R':'1'})
sum_ids = 0
min_id = sys.maxsize
max_id = 0
with open(sys.argv[1]) as f:
    for line in f:
        s = line.strip().translate(tr)
        if s:
            sid = int(s, 2)
            sum_ids += sid
            if sid < min_id: min_id = sid
            if sid > max_id: max_id = sid
expected = (max_id - min_id + 1) * (min_id + max_id) // 2
print(max_id, expected - sum_ids)