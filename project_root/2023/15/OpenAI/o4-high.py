import sys
ord_ = ord
with open(sys.argv[1]) as f:
    words = f.read().strip().split(",")
boxes = [{} for _ in range(256)]
t1 = 0
for w in words:
    h = 0
    for c in w:
        h = ((h + ord_(c)) * 17) & 255
    t1 += h
    if "=" in w:
        l,v = w.split("=",1)
        boxes[h][l] = int(v)
    else:
        boxes[h].pop(w.split("-",1)[0], None)
t2 = 0
for i,b in enumerate(boxes,1):
    for idx,v in enumerate(b.values(),1):
        t2 += i*idx*v
sys.stdout.write(f"{t1} {t2}")