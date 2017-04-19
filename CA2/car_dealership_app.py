"""
App to run Car Dealership programme.

"""

#import all the methods from the different Car Type classes and CarFleet class
from car_fleet import PetrolCar, DieselCar, HybridCar, ElectricCar, CarFleet

#create an instance of each imported class to allow us to access the relevant methods and class variables
aungierCarFleet = CarFleet()
petrolCar = PetrolCar()
dieselCar = DieselCar()
hybridCar = HybridCar()
electricCar = ElectricCar()

#processRental function that calls popCar method in CarFleet class                  
def processRental(carType):
    if carType == 1 and petrolCar.getNumPetrolCars() > 0: #must have at least one petrol car available
        aungierCarFleet.popCar('petrol', aungierCarFleet.petrolCars)
        petrolCar.setNumPetrolCars(len(aungierCarFleet.petrolCars)) #reduce the number of petrol cars
    elif carType == 2 and dieselCar.getNumDieselCars() > 0: #must have at least one diesel car available
        aungierCarFleet.popCar('diesel', aungierCarFleet.dieselCars)
        dieselCar.setNumDieselCars(len(aungierCarFleet.dieselCars)) #reduce the number of diesel cars
    elif carType == 3 and hybridCar.getNumHybridCars() > 0: #must have at least one bybrid car available
        aungierCarFleet.popCar('hybrid', aungierCarFleet.hybridCars)
        hybridCar.setNumHybridCars(len(aungierCarFleet.hybridCars)) #reduce the number of hybrid cars
    elif carType == 4 and electricCar.getNumElectricCars() > 0: #must have at least one electric car available
        aungierCarFleet.popCar('electric', aungierCarFleet.electricCars)
        electricCar.setNumElectricCars(len(aungierCarFleet.electricCars)) #reduce the number of electric cars
    else:
        print 'Sorry but there are no cars of this type available. \nCan you please choose a different car type.'

#processReturn function that calls appendCar method in CarFleet class                  
def processReturn(carType):
    if carType == 1 and petrolCar.getNumPetrolCars() < 20: #cannot have more than 20 petrol cars
        aungierCarFleet.appendCar('petrol', aungierCarFleet.petrolCars, PetrolCar())
        petrolCar.setNumPetrolCars(len(aungierCarFleet.petrolCars)) #increase the number of petrol cars
    elif carType == 2 and dieselCar.getNumDieselCars() < 8: #cannot have more than 8 diesel cars
        aungierCarFleet.appendCar('diesel', aungierCarFleet.dieselCars, DieselCar())
        dieselCar.setNumDieselCars(len(aungierCarFleet.dieselCars)) #increase the number of diesel cars
    elif carType == 3 and hybridCar.getNumHybridCars() < 8: #cannot have more than 8 hybrid cars
        aungierCarFleet.appendCar('hybrid', aungierCarFleet.hybridCars, HybridCar())                             
        hybridCar.setNumHybridCars(len(aungierCarFleet.hybridCars)) #increase the number of hybrid cars
    elif carType == 4 and electricCar.getNumElectricCars() < 4: #cannot have more than 4 electric cars
        aungierCarFleet.appendCar('electric', aungierCarFleet.electricCars, ElectricCar())
        electricCar.setNumElectricCars(len(aungierCarFleet.electricCars)) #increase the number of electric cars
    else:
        print 'The car type is incorrect. Can you please confirm what car type you are returning?'

#keep prompting the user to provide input until they choose to exit the programme
while True:
    
    choice = str(raw_input("Are you looking to rent or return a car? Enter 'rent', 'return' or 'done' to exit the programme: "))
    
    #if the user wants to rent a car check for availability and prompt them to select a car type
    if choice.lower() == 'rent':    
        if aungierCarFleet.numberCarsAvailable == 0:
            print 'Sorry but we have no cars available for rent today!\nPlease try again tomorrow.'
            break
        else:    
            print("What type of car would you like to rent?")
            input = raw_input("Enter '1' for Petrol, '2' for Diesel, '3' for Hybrid or '4' for Electric: ")
            carType = int(input)
            processRental(carType) #pass the car type selected to processRental
            print 'Total cars remaining in the fleet: {}'.format(aungierCarFleet.numberCarsAvailable)
               
    #if the user wants to return a car check that the car has been rented and prompt them to select a car type
    elif choice.lower() == 'return': 
         if aungierCarFleet.numberCarsAvailable == 40:
            print 'Sorry but you must be in the wrong rental office. We have no cars rented at the moment.'
            break
         else:    
            print("What type of car are you returning?")
            input = raw_input("Enter '1' for Petrol, '2' for Diesel, '3' for Hybrid or '4' for Electric: ")
            carType = int(input)
            processReturn(carType) #pass the car type selected to processReturn
            print 'Total cars remaining in the fleet: {}'.format(aungierCarFleet.numberCarsAvailable)
                
    #allow the user to terminate the programme
    elif choice.lower() == 'done':
        print 'You are now exiting the programme...' 
        break


         
  
        
     
    
