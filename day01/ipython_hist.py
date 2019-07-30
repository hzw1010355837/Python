print('PyDev console: using IPython 7.6.1\n')

import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['I:\\score', 'I:/score'])
f = open("./gameover.wav", "rb")
# f = open("./Python/day01/gameover.wav", "rb")
f.read(44)
import struct
info = f.read(44)
# info
f.seek(0)
f.read()
f.seek(0)
info = f.read(44)
# struct.unpack?
# struct.unpack("int", info[12:16])
struct.unpack("i", info[12:16])
struct.unpack("i", info[40:44])
f.seek(0, 2)
f.tell()
result = (f.tell()-44)/2
import array
# array.array?
# array.array("h", result)
# buf = array.array("h", (0 for _ in range(result)))
struct.unpack('h', info[34:36])
# result
buf = array.array("h", (0 for _ in range(int(result))))
# buf
f.seek(44)
f.readinto(buf)
# buf[0]
# for i in range(result): buf[i] /= 8
# for i in range(result):
#     buf[i] /= float(8)
# for i in range(result):
#     buf[i] //= float(8)
# for i in range(result):
#     buf[i] = float(buf[i] / float(8))
# for i in range(int(result)
#                ): buf[i] /= 8
# for i in range(int(result)
#                ): buf[i] /= float(8)
# for i in range(int(result)): buf[i] /= float(8)
# for i in range(int(result)): buf[i] /= 8
for i in range(int(result)): buf[i] //= 8
f1 = open("gameoverUp.wav", "wb")
f1.write(info)
buf.tofile(f1)
f1.close()
# %hist -f ipython_hist.py
