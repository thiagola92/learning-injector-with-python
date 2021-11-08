class FirstClass:
    def __init__(self):
        self.example = 100
    

class SecondClass:
    def __init__(self, fc : FirstClass):
        self.fc = fc
    
fc = FirstClass()
sc = SecondClass(fc)
print(sc.fc.example)