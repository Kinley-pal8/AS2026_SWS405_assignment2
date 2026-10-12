# raw2png.py <dump> <offset> <width> <height> <out.png> [bpp=4]  -- renders raw pixel bytes as grayscale PNG
import sys,zlib,struct
f,off,w,h,out=sys.argv[1],int(sys.argv[2],0),int(sys.argv[3]),int(sys.argv[4]),sys.argv[5]
bpp=int(sys.argv[6]) if len(sys.argv)>6 else 4
d=open(f,'rb'); d.seek(off); buf=d.read(w*h*bpp)
rows=b''
for y in range(h):
    r=buf[y*w*bpp:(y+1)*w*bpp]
    rows+=b'\x00'+bytes(r[x*bpp] for x in range(len(r)//bpp)).ljust(w,b'\x00')
def ch(t,x): return struct.pack('>I',len(x))+t+x+struct.pack('>I',zlib.crc32(t+x)&0xffffffff)
open(out,'wb').write(b'\x89PNG\r\n\x1a\n'+ch(b'IHDR',struct.pack('>IIBBBBB',w,h,8,0,0,0,0))+ch(b'IDAT',zlib.compress(rows))+ch(b'IEND',b''))
