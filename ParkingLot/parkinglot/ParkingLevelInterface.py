from abc import ABC


class ParkingLevel(ABC):
    def is_slot_available(self):
        pass

    def is_vehicle_available(self,*args):
        pass

    def where_is_the_vehicle(self,*args):
        pass

