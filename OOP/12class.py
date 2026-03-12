class Vector: # It's standard convention to capitalize class names
    def __init__(self, x, y, z): # Fixed the trailing underscores here
        self.x = x
        self.y = y
        self.z = z
       
    def sum(self, v):
        # This returns a new Vector instance
        return Vector((self.x + v.x), (self.y + v.y), (self.z + v.z))  

    def result(self):
        return f"sum={self.x},{self.y},{self.z}"
    
    def __add__(self, v):
       return Vector((self.x+v.x),(self.y+v.y),(self.z+v.z))
       
v1 = Vector(3, 2, 4)
v2 = Vector(0, 5, 6)
# v = v1.sum(v2)
v=v1+v2
print(v.result())
