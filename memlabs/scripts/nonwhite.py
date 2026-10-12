import sys
d=open(sys.argv[1],'rb').read(); s=int(sys.argv[2],0); n=int(sys.argv[3])
idx=[i for i in range(s,s+n,4) if d[i:i+3]!=b'\xff\xff\xff']
print(len(idx), [hex(x) for x in idx[:5]], [hex(x) for x in idx[-5:]])
from collections import Counter
print(Counter(d[i:i+4].hex() for i in idx).most_common(6))
