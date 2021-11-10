from injector import inject, Injector, Binder


class FirstClass:
    def __init__(self, number):
        self.example = number


class SecondClass:
    @inject
    def __init__(self, fc: FirstClass):
        self.fc = fc


class ThirdClass:
    @inject
    def __init__(self, sc: SecondClass):
        self.sc = sc


class FourthClass:
    @inject
    def __init__(self, tc: ThirdClass):
        self.tc = tc


def configure(binder):
    binder.bind(FirstClass, to=FirstClass(100))


injector = Injector(configure)
fc = injector.get(FourthClass)
print(fc.tc.sc.fc.example)
