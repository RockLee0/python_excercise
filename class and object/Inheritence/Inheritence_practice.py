class animal:
    def general_purpose(self):
        print('we are animal')

class dog:
    def purpose(self):
        print('we do ghew ghew all the time')

class human(animal,dog):
    def __init__(self):
        self.hand=4
        self.dick=2


    def purposee(self):
        print(f'we only do masterbedroom with {self.hand} hand and {self.dick} lolopopstar')
        super().general_purpose()


tom=dog()
print(tom.purpose())


murzan=human()
print(murzan.purposee())