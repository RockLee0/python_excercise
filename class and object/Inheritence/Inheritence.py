class banor:
    def general(self):
        self.tails='Thay have tails'
        self.mentality='They are rude'
        print(f'they have this mentality which is {self.mentality}')

class human(banor):  #use other class characteristics for using (that class)
    def __init__(self):
        self.legs=5
        self.dicksize=1
        self.backbone = 'stand straight'
        self.family = 'have a family but cheats frequently with others'
    def skill(self):
        print(f'he has {self.legs} legs and {self.family} ')



rony=human()
print(rony.skill())
print(rony.general())