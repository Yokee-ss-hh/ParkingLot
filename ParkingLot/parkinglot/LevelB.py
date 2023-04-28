from parkinglot.ParkingLevelInterface import ParkingLevel


class LevelB(ParkingLevel):
    MAX_CAPACITY = 20
    VEHICLE_DATA = dict()
    CURRENT_CAPACITY = 0

    def __init__(self):
        pass

    def is_slot_available(self):
        return LevelB.CURRENT_CAPACITY < LevelB.MAX_CAPACITY

    @staticmethod
    def is_vehicle_available(vehicle_number):
        return LevelB.VEHICLE_DATA.get(vehicle_number, False)

    def where_is_the_vehicle(self,vehicle_number):
        return self.VEHICLE_DATA[vehicle_number]

