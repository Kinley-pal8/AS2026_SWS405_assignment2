import sys
d=open(sys.argv[1],'rb').read(); B=65536
for i in range(0,len(d),B):
    c=d[i:i+B]; w=c.count(b'\xff\xff\xff')/(len(c)/3); k=c.count(b'\x00\x00\x00\xff')*4/len(c)
    if w>0.4 and k>0.01: print(hex(i), round(w,2), round(k,3))
