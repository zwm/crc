import os
import sys

# macro
CRC_LEN = 7
CRC_INIT = int("0x00", 16)
CRC_POLY = int("0x89", 16)

# file
if len(sys.argv) != 2:
    print("Error: argument 'only one file name' not meet!")
    exit(0)
with open(sys.argv[1]) as f:
    # label
    print("File: %s, open success!" % sys.argv[1])
    # get bit num
    bit_num = f.readline()
    bit_num = bit_num.strip()
    bit_num = int(bit_num)
    # get byte num
    if (bit_num & 7) == 0:
        byte_num = int(bit_num/8) + 0
    else:
        byte_num = int(bit_num/8) + 1
    print("bit_num: %d, byte_num: %d" % (bit_num, byte_num))
    # read byte
    dat = []
    for i in range(byte_num):
        line = int(f.readline().strip(), 16)
        dat.append(line)
# dat
print(dat)
# crc
crc = CRC_INIT
for i in range(bit_num):
    # get idx
    bit_idx = 7 - i%8 # msb first
    byte_idx = int(i/8)
    # din
    din = (dat[byte_idx] >> bit_idx) & 1
    # crc
    crc = (crc << 1) + din;
    msb = (crc >> CRC_LEN) & 1
    if msb == 1:
        crc = crc ^ CRC_POLY
# padding
for i in range(CRC_LEN):
    din = 0
    crc = (crc << 1) + din
    msb = (crc >> CRC_LEN) & 1
    if msb == 1:
        crc = crc ^ CRC_POLY
print("crc: ", hex(crc))





