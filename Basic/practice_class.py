class Unit:
    def __init__(self):
        print("Unit generator")
    
class Flyable:
    def __init__(self):
        print("Flyable generator")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        ## super().__init__() #super()로 init 할 때는 self 필요없음.
        Unit.__init__(self)
        Flyable.__init__(self)

# dropship
dropship = FlyableUnit()

'''
다중상속을 할 때는 super를 쓰면 맨 마지막에 쓰는 상속받는 부모클래스에 대해서만 init함수 호출이 된다.
따라서 모든 부모클래스에 대해 초기화가 필요하다고 하면 super()보다는 각각 호출에서 해줘야함.
'''
