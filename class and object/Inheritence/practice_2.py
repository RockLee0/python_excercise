
class student:
    def general(self):
        print(' i am a student')

class youtuber:
    def general2(self):
        print('i am a youtuber and i make videos')
class teacher:
    def general(self):
        print('got a master degree and now i am a teacher')

class person(student,teacher,youtuber):
    pass

ramzan=person()
ramzan.general()
ramzan.general2()
