class Guest():
    
    dic = {'John' : 'A011', 'Kyle':'A009','Jake':'BQ02','Tamra' :'A015','Josh':'BQ03'}
    kys = ['A010','A012','A012','BQ01']

    def __init__(self,invitado):
        self.name = invitado
    def is_regd(self):
        if self.name in self.dic:
            print('Registered')
        else:
            print('Not Registered')
    def get_key(self):
        if self.name in self.dic:
            print('Key :',self.dic[self.name])
        else:
            print('not registered')
    def reg(self):
        if self.name in self.dic:
            print(self.dic[self.name])
        else:
            if len(self.kys) > 0:
                print('Key :',self.kys.pop())
            else:
                print('Sorry, no vacant rooms available')
        
a = Guest('Josh')
print(a.name)
a.is_regd()
a.get_key()
a.reg()

b = Guest('Hans')
print(b.name)
b.is_regd()
b.get_key()
b.reg()

c = Guest('Evan')
print(c.name)
c.is_regd()
c.get_key()
c.reg()

d = Guest('Kyle')
print(d.name)
d.is_regd()
d.get_key()
d.reg()

e = Guest('Ted')
print(e.name)
e.is_regd()
e.get_key()
e.reg()

f = Guest('Karl')
print(f.name)
f.is_regd()
f.get_key()
f.reg()

g = Guest('Sam')
print(g.name)
g.is_regd()
g.get_key()
g.reg()