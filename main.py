import binascii



f = open('test.gb')

line = f.readline(1)

x = 0
while line:
   # line = line.upper()
    line = binascii.hexlify(line)
    if x < 20 :
        print "{:08b}".format(int('0x' + line, 16))
    line = f.read(1)
    x = x + 1

f.close()
