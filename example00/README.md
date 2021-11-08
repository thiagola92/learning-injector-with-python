# Constructor without parameters
```python
class FirstClass:
    def __init__(self):
        self.example = 100
    

class SecondClass:
    def __init__(self, fc : FirstClass):
        self.fc = fc
    
fc = FirstClass()
sc = SecondClass(fc)
print(sc.fc.example)
```

By default `Injector` will assume that the class doesn't need parameters. It's very easy to use injector in this case:  
```python
from injector import inject, Injector

class FirstClass:
    def __init__(self):
        self.example = 100
    

class SecondClass:
    @inject
    def __init__(self, fc : FirstClass):
        self.fc = fc

injector = Injector()
sc = injector.get(SecondClass)
print(sc.fc.example)
```