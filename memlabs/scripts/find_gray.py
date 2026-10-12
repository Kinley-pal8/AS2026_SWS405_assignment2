import sys
d=open(sys.argv[1],'rb').read(); B=65536
for i in range(0,len(d)-B,B):
    c=d[i:i+B]; n=B//4; g=w=0
    for j in range(0,B,16):
        p=c[j:j+4]
        if p[0]==p[1]==p[2]:
            g+=1
            if p[0]==255: w+=1
    n=B//16
    if g/n>0.97 and 0.3<w/n<0.985: print(hex(i), round(g/n,3), round(w/n,3))
