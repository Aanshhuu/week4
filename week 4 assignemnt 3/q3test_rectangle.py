
from rectangle import Rectangle


rect = Rectangle(10, 5)


print(f"Area: {rect.area()}")          
print(f"Perimeter: {rect.perimeter()}") 

# Setting new values
rect.setWidth(7)
rect.setHeight(3)

# Calling methods again
print(f"New Area: {rect.area()}")         
print(f"New Perimeter: {rect.perimeter()}") 
