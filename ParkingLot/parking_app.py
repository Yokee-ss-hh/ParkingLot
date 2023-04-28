import json

from parkinglot.Vehicle import Vehicle
from parkinglot.NotifyUser import Notify
while(True):
        vehicle_types = {1: "cycle", 2: "bike", 3: "car", 4: "bus", 5: "lorry"}
        modes = {1:"park vehicle", 2:"un park vehicle", 3: "find my vehicle", 4:"exit from application"}
        print("Click 1 to park vehicle, Click 2 to un-park vehicle, Click 3 to find your vehicle, Click 4 to exit from application")
        mode = int(input("***Dear customer, Please select any one of the above options!***"))

        if type(mode) is int and mode in modes and mode == 1:
            u_name = input("Please enter your full name")
            v_num = input("Please enter your vehicle number")
            print("***For cycle enter 1, For bike enter 2, For car enter 3, For bus enter 4, For lorry enter 5***")
            v_type = int(input("***Please enter the above option as per your vehicle type***"))
            p_number = int(input("***Please enter your 10 digit mobile number***"))
            try:
                if type(v_type) is int and type(p_number) is int and v_type in vehicle_types:
                    vehicle = Vehicle(vehicle_number=v_num, user_name=u_name, vehicle_type=vehicle_types[v_type],
                                  phone_number=p_number)
                    data = vehicle.park_vehicle(vehicle.vehicle_number)
                    # Convert python dictionary data to json format
                    print(json.dumps(data,indent=4))
                    # Notifying customer via sms
                    notify = Notify()
                    notify.send_sms(data)
                else:
                    print("Please select valid data, Thanks")
            except Exception as e:
               print(e)

        elif type(mode) is int and mode in modes and mode == 2:
            try:
                vehicle_number = input("Please enter your vehicle number to un-park it!")
                un_parked_vehicle_data = Vehicle.un_park_vehicle(vehicle_number)
                print(un_parked_vehicle_data)
                # Notifying customer via sms
                notify = Notify()
                notify.send_sms(un_parked_vehicle_data)
            except Exception as e:
                print(e)

        elif type(mode) is int and mode in modes and mode == 3:
            try:
                vehicle_number = input("Please enter your vehicle number to find parking details")
                print(Vehicle.spot_my_vehicle(vehicle_number))
            except Exception as e:
                print(e)

        elif type(mode) is int and mode in modes and mode == 4:
            exit()

        else:
            print("Please select the appropriate mode")
