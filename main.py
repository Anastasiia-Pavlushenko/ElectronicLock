class ElectronicLock:
    def __init__(self):
        pass

    def isInProgrammingMode(self):
        pass

    def toggleProgrammingMode(self, programmingCode):
        if not isinstance(programmingCode, int):
            raise TypeError("PC must be int")
        pass

    def registerCode(self, code):
        if not isinstance(code, int):
            raise TypeError("Code must be int")
        pass

    def unregisterCode(self, code):
        if not isinstance(code, int):
            raise TypeError("Code must be int")
        pass

    def changeProgrammingCode(self, code):
        if not isinstance(code, int):
            raise TypeError("Code must be int")
        pass

    def tryUnlocking(self, code):
        if isinstance(code, int):
            pass
        elif isinstance(code, str):
            pass
        else:
            raise TypeError
