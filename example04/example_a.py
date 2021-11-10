class FirstClass:
    def __init__(self, number):
        self.example = number


class SecondClass:
    def __init__(self, fc: FirstClass):
        self.fc = fc


class ThirdClass:
    def __init__(self, sc: SecondClass):
        self.sc = sc


class FourthClass:
    def __init__(self, tc: ThirdClass):
        self.tc = tc


fc = FirstClass(100)
sc = SecondClass(fc)
tc = ThirdClass(sc)
fc = FourthClass(tc)
print(fc.tc.sc.fc.example)
