# Polymorphism

class Gender:
    def __init__(self):
        pass
    
    def doCarryObjects(self):
        pass


class Male(Gender):
    def __init__(self):
        pass

    def doCarryObjects(self):
        print("Carry Heavy Object")


class Female(Gender):
    def __init__(self):
        pass

    def doCarryObjects(self):
        print("Carry Light Object")

def getGender(name):
    if "A/L" in name:
        return Male()
    else:
        return Female()

gender = getGender("Khairi A/L Abu Bakar")
gender.doCarryObjects()
print(type(gender))

gender = getGender("Aida A/P Abu Bakar")
gender.doCarryObjects()
print(type(gender))