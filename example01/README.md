# Constructor without parameters
```python
class FirstClass:
    def __init__(self, number):
        self.example = number
    

class SecondClass:
    def __init__(self, fc : FirstClass):
        self.fc = fc
    
fc = FirstClass(100)
sc = SecondClass(fc)
print(sc.fc.example)
```

If your class needs parameters, you should tell the `Injector` which instance to use.  
The `configure` function will bind any use of "FirstClass" to an instance.  
```python
from injector import inject, Injector, Binder

class FirstClass:
    def __init__(self, number):
        self.example = number
    

class SecondClass:
    @inject
    def __init__(self, fc : FirstClass):
        self.fc = fc


def configure(binder):
    binder.bind(FirstClass, to=FirstClass(100))

injector = Injector(configure)
sc = injector.get(SecondClass)
print(sc.fc.example)
```