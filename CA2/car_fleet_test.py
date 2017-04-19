"""
This class is used to test all our Car and CarFleet functions 
"""

#set up test environment 
import unittest

#import all the methods from the Car and CarFleet classes
from car_fleet import Car, PetrolCar, DieselCar, HybridCar, ElectricCar, CarFleet

class CarFleetTest(unittest.TestCase):
    
    #test to verify setting the car type 
    def testSetCarType(self):
        myCar = Car()
        myCar.setType('petrol')
        self.assertEqual('petrol', myCar.getType())
        myCar.setType('hybrid')
        self.assertEqual('hybrid', myCar.getType())
    
    #test to verify setting the number of petrol cars 
    def testSetNumPetrolCars(self):
        petrolCar = PetrolCar()
        petrolCar.setNumPetrolCars(10)
        self.assertEqual(10, petrolCar.getNumPetrolCars())
        petrolCar.setNumPetrolCars(0)
        self.assertEqual(0, petrolCar.getNumPetrolCars())
        
    #test to verify setting the number of diesel cars 
    def testSetNumDieselCars(self):
        dieselCar = DieselCar()
        dieselCar.setNumDieselCars(8)
        self.assertEqual(8, dieselCar.getNumDieselCars())
        dieselCar.setNumDieselCars(3)
        self.assertEqual(3, dieselCar.getNumDieselCars())
        
    #test to verify setting the number of hybrid cars 
    def testSetNumHybridCars(self):
        hybridCar = HybridCar()
        hybridCar.setNumHybridCars(1)
        self.assertEqual(1, hybridCar.getNumHybridCars())
        hybridCar.setNumHybridCars(5)
        self.assertEqual(5, hybridCar.getNumHybridCars())
        
    #test to verify setting the number of electric cars 
    def testSetNumElectricCars(self):
        electricCar = ElectricCar()
        electricCar.setNumElectricCars(4)
        self.assertEqual(4, electricCar.getNumElectricCars())
        electricCar.setNumElectricCars(2)
        self.assertEqual(2, electricCar.getNumElectricCars())
    
    #test to verify the adding of cars from a specified car list
    def testPopCar(self):
        carFleet = CarFleet()
        petrolCar = PetrolCar()
        carFleet.petrolCars.append(petrolCar)
        self.assertEqual(petrolCar, carFleet.popCar('petrol', carFleet.petrolCars))
    
    #test to verify the adding of cars from a specified car list
    def testAppendCar(self):
        carFleet = CarFleet()
        dieselCar = DieselCar()
        carFleet.dieselCars.append(dieselCar)
        self.assertEqual(10, carFleet.appendCar('diesel', carFleet.dieselCars, DieselCar))
    
    
#run the test program
if __name__ == '__main__':
    unittest.main()