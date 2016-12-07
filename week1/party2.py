class Party2:
    x=0

    def __init__(self):
        print "I am constructued"


    def party(self):
        self.x = self.x+1
        print "so far", self.x


    def __del__(self):
        print "I am destructued", self.x


an = Party2()
an.party()
an.party()
an.party()
