class dbuffer:
    def __init__(self):
        self.MAXSIZE = 2620000
        self.buff = bytes()
        self.len = 0
        self.isFull = False
        self.initialized = False
    
    def initialize(self):
        self.initialized = True

    def addStuff(self, stuff, length):
        self.buff = self.buff + stuff
        self.len = self.len + length
        return

    def remStuff(self,nbytes):
        return self.buff[0:nbytes]

    def __str__(self):
        return 'PRINT FROM THE dbuffer CLASS : ' + str(self.buff)
