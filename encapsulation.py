class car:
    def __init__(self,carname,noofwheels,noofairbags):#constructor
        self.carname=carname#variable
        self.__noofwheels=noofwheels#privatevariable
        self.noofairbags=noofairbags
    def get_no_of_wheels(self):#getter
        return ("no of wheels:",self.__noofwheels)#encapsulation 
    def set_no_of_wheels(self,noofwheels):#setter
        self.__noofwheels=noofwheels
        
c2=car("bmw",4,6)
print(c2.carname,c2.noofairbags,c2.get_no_of_wheels())
print(c2.get_no_of_wheels())
c2.__noofwheels=43
print("new",c2.__noofwheels)
print(c2.get_no_of_wheels())#getting value
c2.set_no_of_wheels(9)#setting valvue 
print(c2.get_no_of_wheels())#printing the setted value using get method 