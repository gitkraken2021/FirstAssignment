class greatgrandfather():
    def greatgrandfatherfn(self):
        print("function of greatgrand father")
class grandfather(greatgrandfather):#single inheritance
    def grandfatherfn(self):
        print("function of grandfather")
class father(grandfather):#multilevel inheritance
    def fatherfn(self):
        print("function of father")

class motheer():#No inheritance
    def motherfn(self):
        print("function of mother")

class Son(father,motheer):  #Hybrid Inherritance
    def sonfn(self):
        print("this is function of Son")

object=Son()
object.sonfn()
object.fatherfn()
object.motherfn()
object.grandfatherfn()
object.greatgrandfatherfn()

