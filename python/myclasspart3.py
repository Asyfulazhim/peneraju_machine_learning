# encapsulation the properties inside the class
# inheritance the properties of one class to another classi
# in other languange we have keywords public, private, protected
# in python we have _ (single underscore) and __ (double underscore)
# _ (single underscore) is used for private properties
# __ (double underscore) is used for protected properties

class circle:

    def __init__(self, radius):
        # change the property with single underscore
        # this make the property private
        self._radius = radius
        #self.radius = radius
        if (isinstance(radius, int)):
            self._radius = radius
        else:
            raise TypeError("radius must be an integer")
        
    # getter method and setter method
    def get_radius(self):
        print(self._radius)
        return self._radius
    
    def set_radius(self, radius):
        if (isinstance(radius, int)):
            self._radius = radius
            print("Set Radius", self._radius)
        else:
            raise TypeError("radius must be an integer")

    # bracket when pasing getter and setter
    # property class returns the property object which is assigned to a variable value
    # in other words radius is an istance of property class

    radius = property(get_radius, set_radius)

    def area(self):
        return 3.14 * self._radius * self._radius
    
    def circumference(self):
        return 2 * 3.14 * self._radius
    
mycircle = circle(20)
print(mycircle.area())
print(mycircle.circumference())
mycircle.get_radius()
mycircle.set_radius(30)
mycircle.radius = 40
#mycircle = circle("abc")

# you are directly ....
mycircle._radius = "abc"
print(mycircle)

# dont use double and single underscore outside of the class