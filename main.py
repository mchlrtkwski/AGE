import binascii
from view import View
from memory import Memory




#f = open('bios.gb')

#line = f.readline(1)

#x = 1
#while line:
   # line = line.upper()
   # line = binascii.hexlify(line)

    #print  str(x) + " " + "{:08b}".format(int('0x' + line, 16))
   ##x = x + 1;

#f.close()
#new2 = Memory()
#new = View()
gbMemory = Memory()
gbMemory.printHexMemDump()
