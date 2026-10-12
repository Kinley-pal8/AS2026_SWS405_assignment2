import sys
d=open(sys.argv[1],'rb').read()
B=65536
runs=[];start=None
for i in range(0,len(d),B):
    c=d[i:i+B]; w=c.count(b'\xff')/len(c)
    if w>0.85:
        if start is None: start=i
    else:
        if start is not None: runs.append((i-start,start)); start=None
runs.sort(reverse=True)
for l,s in runs[:8]: print(hex(s), l, l//4)
