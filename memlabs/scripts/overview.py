# overview.py dump width step out_prefix rows_per_tile : downsampled grayscale overview of a raw dump (4 bytes/pixel)
import sys,zlib,struct
f,w,st,pre,rpt=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),sys.argv[4],int(sys.argv[5])
d=open(f,'rb').read(); row=w*4; nrows=len(d)//row
def ch(t,x): return struct.pack('>I',len(x))+t+x+struct.pack('>I',zlib.crc32(t+x)&0xffffffff)
ow=w//st; tile=0
for t0 in range(0,nrows,rpt*st):
    rows=b''; h=0
    for y in range(t0,min(nrows,t0+rpt*st),st):
        r=d[y*row:(y+1)*row]; rows+=b'\x00'+bytes(r[x*4*st] for x in range(ow)); h+=1
    open('%s_%02d.png'%(pre,tile),'wb').write(b'\x89PNG\r\n\x1a\n'+ch(b'IHDR',struct.pack('>IIBBBBB',ow,h,8,0,0,0,0))+ch(b'IDAT',zlib.compress(rows))+ch(b'IEND',b''))
    print(tile, hex(t0*row)); tile+=1
