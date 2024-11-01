class Monostate:
    _shared_state = {}
    
    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args,**kwargs)
        obj.__dict__ = cls._shared_state
        return obj
    
class CFO(Monostate):
    def __init__(self):
        self.name = ''
        self.money_managed = 0
    
    def __str__(self):
        return f"{self.name} manages {self.money_managed}bn"
    
if __name__ == '__main__':
    cfo1 = CFO()
    cfo1.name = 'Shery1'
    cfo1.money_managed = 1
    print(cfo1)
    
    cfo2 = CFO()
    cfo2.name = 'Ruth'
    cfo2.money_managed = 10
    print(cfo1, cfo2, sep='\n')