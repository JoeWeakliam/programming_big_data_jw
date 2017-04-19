"""
Car programme that contains all relevant Car and Car Fleet classes

"""
#create Car class
class Car(object):
    
    def __init__(self):
        self.__colour = '' #private instance variables
        self.__make = ''
        self.__type = ''
                
    def setType(self, value): #set the type of the Car object
        self.__type = value
    
    def getType(self):
        return self.__type #return the type of the Car object
    
#create class PetrolCar that extends class Car
class PetrolCar(Car):
    
    def __init__(self):
        self.setType('Petrol') #set the type
        self.__numPetrolCars = 20 #set the number of petrol cars to 20 to begin
    
    def setNumPetrolCars(self, number):
        self.__numPetrolCars = number
    
    def getNumPetrolCars(self):
        return self.__numPetrolCars
    
#create class DieselCar that extends class Car
class DieselCar(Car):
    
    def __init__(self):
        self.setType('Diesel') #set the type
        self.__numDieselCars = 8 #set the number of diesel cars to 8 to begin
    
    def setNumDieselCars(self, number):
        self.__numDieselCars = number
    
    def getNumDieselCars(self):
        return self.__numDieselCars
    
#create class HybridCar that extends class Car
class HybridCar(Car):
    
    def __init__(self):
        self.setType('Hybrid') #set the type
        self.__numHybridCars = 8 #set the number of hybrid cars to 8 to begin
    
    def setNumHybridCars(self, number):
        self.__numHybridCars = number
    
    def getNumHybridCars(self):
        return self.__numHybridCars
        
#create class ElectricCar that extends class Car
class ElectricCar(Car):
    
    def __init__(self): 
        self.setType('Electric') #set the type
        self.__numElectricCars = 4 #set the number of electric cars to 4 to begin
    
    def setNumElectricCars(self, number):
        self.__numElectricCars = number
    
    def getNumElectricCars(self):
        return self.__numElectricCars
    
#create class CarFleet to manage the fleet of rental cars and create the current stock
class CarFleet(object):
    
    #function to create and populate lists to manage rental fleets of each car type
    def __init__(self):
        self.numberCarsAvailable = 40 #total number of cars available to rent in fleet
        self.petrolCars = []
        self.dieselCars = []
        self.hybridCars = []
        self.electricCars = []
        for x in range(1,21):
            self.petrolCars.append(PetrolCar()) #50% of the cars are petrol
        for x in range(1,9):
            self.dieselCars.append(DieselCar()) #20% of the cars are diesel
            self.hybridCars.append(HybridCar()) #20% of the cars are hybrid
        for x in range(1,5):
            self.electricCars.append(ElectricCar()) #10% of the cars are electric
        
        #show what cars are available to rent when we create an instance of the CarFleet class
        print 'There are {} petrol cars in the fleet'.format(len(self.petrolCars))
        print 'There are {} diesel cars in the fleet'.format(len(self.dieselCars))
        print 'There are {} hybrid cars in the fleet'.format(len(self.hybridCars))
        print 'There are {} electric cars in the fleet'.format(len(self.electricCars))
    
    #function popCar reduces the number of cars within a specific car list      
    def popCar(self, carType, carList):
        pop_value = carList.pop()
        self.numberCarsAvailable -= 1 #reduce the total stock by 1
        print 'Your request for a {} car has been granted. Have a safe journey.'.format(carType)
        print 'Number of {} cars now available: {}'.format(carType, len(carList))
        return pop_value #included to allow test to run
        
    #function appendCar increases the number of cars within a specific car list             
    def appendCar(self, carType, carList, carObject):       
        carList.append(carObject)
        self.numberCarsAvailable += 1 #increase the total stock by 1
        print 'Thanks for returning the car. Have a nice day!' 
        print 'Number of {} cars now available: {}'.format(carType, len(carList))
        return len(carList) #included to allow test to run
    