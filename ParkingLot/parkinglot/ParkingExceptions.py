class VehicleAlreadyAvailableInLevelException(Exception):
    def __init__(self,message):
        self.message = message


class SlotsAreCompletelyFilledException(Exception):
    def __init__(self,message):
        self.message = message


class VehicleUnAvailableException(Exception):
    def __init__(self,message):
        self.message = message
