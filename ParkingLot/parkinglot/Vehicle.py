from parkinglot.LevelA import LevelA
from parkinglot.LevelB import LevelB
from parkinglot.ParkingExceptions import VehicleUnAvailableException, VehicleAlreadyAvailableInLevelException, SlotsAreCompletelyFilledException
levelA = LevelA()
levelB = LevelB()


class Vehicle:

    def __init__(self, vehicle_number, vehicle_type, user_name, phone_number):
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type
        self.user_name = user_name
        self.phone_number = phone_number

    def park_vehicle(self,vehicle_number):
        if levelA.is_slot_available():
            if not levelA.is_vehicle_available(vehicle_number):
                LevelA.CURRENT_CAPACITY = LevelA.CURRENT_CAPACITY+1
                current_available_spot_level_a = LevelA.CURRENT_CAPACITY
                LevelA.VEHICLE_DATA[str(vehicle_number)] = dict(level='A', spot=current_available_spot_level_a, user_name=self.user_name, phone_number=self.phone_number, vehicle_type=self.vehicle_type)
                return f"Dear customer your vehicle is parked successfully at level A and slot number {current_available_spot_level_a}"
            else:
                raise VehicleAlreadyAvailableInLevelException("Vehicle with this vehicle number is already parked")

        elif levelB.is_slot_available():
            if not levelB.is_vehicle_available(vehicle_number):
                LevelB.CURRENT_CAPACITY = LevelB.CURRENT_CAPACITY+1
                current_available_spot_level_b = LevelB.CURRENT_CAPACITY
                LevelB.VEHICLE_DATA[str(vehicle_number)] = dict(level='B', spot=current_available_spot_level_b, user_name=self.user_name, phone_number=self.phone_number, vehicle_type=self.vehicle_type)
                return f"Dear customer your vehicle is parked successfully at level B and slot number {current_available_spot_level_b}"
            else:
                raise VehicleAlreadyAvailableInLevelException("Vehicle with this vehicle number is already parked")

        else:
            raise SlotsAreCompletelyFilledException("Slots are completely filled now! Please try again later after sometime")

    @staticmethod
    def un_park_vehicle(vehicle_number):
        if levelA.is_vehicle_available(vehicle_number):
            vehicle_data = levelA.VEHICLE_DATA[vehicle_number]
            levelA.VEHICLE_DATA.pop(vehicle_number)
            LevelA.CURRENT_CAPACITY -= 1
            return f"The vehicle with vehicle number {vehicle_number} is un_parked successfully by the customer"

        elif levelB.is_vehicle_available(vehicle_number):
            vehicle_data = levelB.VEHICLE_DATA[vehicle_number]
            levelB.VEHICLE_DATA.pop(vehicle_number)
            LevelB.CURRENT_CAPACITY -= 1
            return f"The vehicle with vehicle number {vehicle_number} is un_parked successfully by the customer"

        else:
            raise VehicleUnAvailableException("OOPS! The vehicle with this vehicle number is not parked with us!!")

    @staticmethod
    def spot_my_vehicle(vehicle_number):
        if levelA.is_vehicle_available(vehicle_number):
            return levelA.where_is_the_vehicle(vehicle_number)

        if levelB.is_vehicle_available(vehicle_number):
            return levelB.where_is_the_vehicle(vehicle_number)

        else:
            raise VehicleUnAvailableException("OOPS! The vehicle with this vehicle number is not parked with us!!")

