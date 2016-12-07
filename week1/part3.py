class Party3:
    x=0
    name=""

    def __init__(self, name):
        self.name=name
        print self.name,"constructued"


    def party(self):
        self.x = self.x+1
        print self.name,"party count", self.x

s = Party3("Sally")
s.party()

j = Party3("Jim")
j.party()
s.party()
