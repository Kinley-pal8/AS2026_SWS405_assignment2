# Reverses evilscript.py: vip.txt = base64( each char XOR 3 )  ->  base64-decode, then XOR each byte with 3
import base64, sys
data = open(sys.argv[1], 'rb').read().rstrip(b'\x00').strip()
print(''.join(chr(b ^ 3) for b in base64.b64decode(data)))
