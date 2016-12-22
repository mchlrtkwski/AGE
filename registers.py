
class Registers:

    regA = int("0,00", 16)
    regF = int("0,00", 16)
    regB = int("0,00", 16)
    regC = int("0,00", 16)
    regD = int("0,00", 16)
    regE = int("0,00", 16)
    regH = int("0,00", 16)
    regL = int("0,00", 16)
    regSP = int("0,0000", 16)
    regPC = int("0,0000", 16)

    ZERO_FLAG = 7
    SUBTRACT_FLAG = 6
    HALF_CARRY_FLAG = 5
    CARRY_FLAG = 4

    def init(self):
        regSp = int("0x0100", 16)