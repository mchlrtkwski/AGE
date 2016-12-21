########################################################################################################################
# memory.py
# This class contains all the memory available to the emulator
# encapsulated into an list.
########################################################################################################################


import binascii


class Memory:

    BIOS_LOCATION = "bios.gb"
    TOTAL_MEMORY_ADDRESSES = int('ffff', 16)
    memoryArray = [int('0x0', 16)] * TOTAL_MEMORY_ADDRESSES

    def __init__(self):
        self.loadBios()

    ####################################################################################################################
    # The loadBios function reads through each hexadecimal value of the bios and places it into the next slot of the
    # memory list.
    ####################################################################################################################
    def loadBios(self):
        try:
            biosFile = open(self.BIOS_LOCATION)
            address = biosFile.readline(1)
            location = 0;
            while address:
                self.memoryArray[location] = int(binascii.hexlify(address), 16)
                address = biosFile.read(1)
                location = location + 1
            biosFile.close()
        except:
            print "COULD NOT LOAD BIOS"

    ####################################################################################################################
    # The printHexDump function print out every memory address in hex format.
    ####################################################################################################################
    def printHexMemDump(self):
        index = 0
        while index < self.TOTAL_MEMORY_ADDRESSES:
            print "0x" + "{:04x}".format(index, '#04x') + " " + format(self.memoryArray[index], '02x')
            index = index + 1

    ####################################################################################################################
    # The printHexDump function print out every memory address in binary format.
    ####################################################################################################################

    def printBinMemDump(self):
        index = 0
        while index < self.TOTAL_MEMORY_ADDRESSES:
            print "0x" + "{:04x}".format(index, '#04x') + " " + "{:08b}".format(self.memoryArray[index])
            index = index + 1

    ####################################################################################################################
    # The initializeMem function places a default 0 into each list slot.
    ####################################################################################################################
    def initializeMem(self):
        index = 0
        while index < self.TOTAL_MEMORY_ADDRESSES:
            self.memoryArray[index] = 0;
            index = index + 1

