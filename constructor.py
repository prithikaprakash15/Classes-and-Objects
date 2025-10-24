'''class car1:
    def __init__(self):
        print("this is a constructor")
c=car1()
print(c)'''

class car:
    def __init__(self,carname,noofwheels,noofairbags):#constructor
        self.carname=carname#variable
        self.noofwheels=noofwheels
        self.noofairbags=noofairbags
    def __str__(Self):
        return (Self,c2.carname)    
c=car("mercedes",4,5)#object-instance of a class
print(c.carname,c.noofairbags,c.noofwheels)
c2=car("bmw",4,6)
print(c2.carname,c2.noofairbags,c2.noofwheels)  
def forward():
    print("the car is moving forward")#methods
forward()
c2.carname="swift"
print("the new carname is:",c2.carname)

     