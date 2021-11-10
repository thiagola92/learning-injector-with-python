# Constructor without parameters
```python
class FirstClass:
    def __init__(self, number):
        self.example = number


class SecondClass:
    def __init__(self, fc: FirstClass):
        self.fc = fc


class ThirdClass:
    def __init__(self, sc: SecondClass):
        self.sc = sc


fc = FirstClass(100)
sc = SecondClass(fc)
tc = ThirdClass(sc)
print(tc.sc.fc.example)
```

The more the code grows, the more advantage you can see.  
```python
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


def configure(binder):
    binder.bind(FirstClass, to=FirstClass(100))


injector = Injector(configure)
tc = injector.get(ThirdClass)
print(tc.sc.fc.example)
```