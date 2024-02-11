from SoupLangage import SoupConfiguration


class AliceBobPeterson(SoupConfiguration):
    def __init__(self):
        self.state_Alice = 0   #0,1,2
        self.state_Bob = 0
        self.flag_Alice = 0
        self.flag_Bob = 0
        self.turn=-1    #-1 personne, 0: Alice, 1:Bob

    def __hash__(self):
        return hash(self.state_Alice + self.state_Bob+ self.flag_Alice +self.flag_Bob )

    def __eq__(self, other):
        return self.state_Alice == other.state_Alice and self.state_Bob == other.state_Bob and self.flag_Alice == other.flag_Alice and self.flag_Bob == other.flag_Bob and self.turn==other.turn

    def __str__(self):
        return "Alice: "+str(self.state_Alice)+" flag alice: "+str(self.flag_Alice) +" Bob: "+ str(self.state_Bob)+" flag Bob: "+str(self.flag_Bob)