
class LogicGate:
    
    def __init__(self,n):
        self.label = n
        self.output = None
        
    def getLabel(self):
        return self.label
    
    def getOutput(self):
        return self.output
    

class BinaryGate(LogicGate):
    
    def __init__(self,n):
        super().__init__(n)
        
        self.pinA = None
        self.pinB = None
        
    def setPinA(self, m):
        self.pinA = m
        
    def setPinB(self, m):
        self.pinB = m
        
    def setNexPin(self,source):
        if self.pinA == None:
            self.pinA == source
        else: 
            if self.pinB == None:
                self.pinB == source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")
    
    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate " + self.getLabel() + "--->"))
        else:
            return self.pinA
    
    def getPinB(self):
        return int(input("Enter Pin B input for gate " + self.getLabel() + "--->"))
    



class UnaryGate(LogicGate):
    def __init__(self,n,pin_val):
        super().__init__(n)
        self.pin = pin_val
        
    def setPin(self, m):
        self.pin = m
        
    
    def getPin(self):
        return self.pin
    

class AndGate(BinaryGate):
    
    def __init__(self, n):
        super().__init__(n)
    
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        
        if a == 1 and b == 1:
            return 1
        else: 
            return 0


class Connector:
    
    from_gate: LogicGate
    to_gate: LogicGate
    
    def __init__(self,fgate,tgate):
        self.from_gate = fgate
        self.to_gate = tgate
        tgate.setNextPin(self)
        
    def getFrom(self):
        return self.from_gate
    
    def getTo(self): 
        return self.to_gate
    

g1 = AndGate("G1")

print(g1.performGateLogic())

