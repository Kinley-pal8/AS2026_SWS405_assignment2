import sys
d=open(sys.argv[1],'rb').read(); s=int(sys.argv[2],0); n=int(sys.argv[3])
m=[1 if d[i]!=255 else 0 for i in range(s,s+n*4,4)]
res=[]
for lag in range(300,3000):
    c=sum(m[i]&m[i+lag] for i in range(0,len(m)-lag,3)); res.append((c,lag))
res.sort(reverse=True); print(res[:10])
