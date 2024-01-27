class Mtca:
    priniciple='Mr prabakar Naidu'
    college='MTCA'
    location='palamaner'
    def__init__(self,name,mob,email,sem):
        self.name='name'
        self.mobile='mob'
        self.emal='email'
        self.sem='sem'
    def udate_mob(self,new):
       self.mobile=new
       print('mobile number updated')
    @classmethod
    def change_priniciple(cls,new):
       cls.princialpal=new
    @staticmethod
    def add(a,b):
      return a+b
roopa=Mtca('roopa',65567787654,'roopa2gmail.com',1)         
    
    