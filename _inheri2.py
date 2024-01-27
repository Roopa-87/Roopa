class Mtca:
    chairman='Mr.Sunil'
    loction='palamaner'
    college='MTCA'
    def __init__(self,name,mobile):
        self.name=name
        self.mobile=mobile
class Mca(Mtca):
    principal=' Mr.prabakar '
    strength=240
    staff=9
class Btech(Mtca):
    principal='Ms.Roopa'    
    strength=326
    staff=76
Teja=Mca('Teja',6786554443)    
Sri=Mca('Sri',876555432)