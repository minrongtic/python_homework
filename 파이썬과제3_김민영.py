class Tooniverse:
    def __init__(self, name, age, gender):
        self.team="투니버스 사랑단"
        self.name=name
        self.age=age
        self.gender=gender

    def info(self):
        print("%s는 %d세이고, %s입니다." %(self.name, self.age, self.gender))

    def intro(self):
        print("%s은 %d세이고, %s입니다." %(self.name, self.age, self.gender))

zg=Tooniverse("짱구", 5, "남자")
dr=Tooniverse("도라에몽", 14, "남자")
cn=Tooniverse("코난", 8, "남자")
cc=Tooniverse("쇼콜라", 15, "여자")
am=Tooniverse("아무", 12, "여자")
gy=Tooniverse("가영", 16, "여자")

zg.info()
dr.intro()
cn.intro()
cc.info()
am.info()
gy.intro()    
