# ParkingLot

<h2>Project Structure</h2>
![Alt image](https://user-images.githubusercontent.com/82704862/235039713-0768f97d-6c07-43fd-bfda-0c5625ed9b80.png)
<h2>Project implementation highlights</h2>
  <ol>
    <li>Classes for parking levels: LevelA and LevelB are totally dedicated to available levels in parking lot with their maximum available and current available slots</li>
    <li>Class for parking, un-parking and finding parked vehicle: Vehicle class with 3 methods</li>
    <li>Methods available in Vehicle class: park_vehicle(*args), un_park_vehicle(*args) and spot_my_vehicle(*args) where args is vehicle_number</li>
    <li>Custom exception classes: VehicleAlreadyAvailableInLevelException, SlotsAreCompletelyFilledException and VehicleUnAvailableException</li> 
    <li>Notify class: This class is used to send sms text to customer of parked vehicle details</li>
  </ol>
<h2>Methods of Vehicle class in the project </h2>
<ol>
<li><h4> park_vehicle(*args) takes vehicle number as a parameter and stores the vehicle and it's user information such as vehicle type, customer name, phone number and returns a data string</h4></li>
<li><h4> remove_vehicle(*args) takes vehicle number as a parameter and removes the vehicle from memory and returns a data string</h4></li>
<li><h4> spot_my_vehicle(*args) takes vehicle number as a parameter and returns the JSON data consisting of the vehicle parked level, parked slot etc </h4></li>
</ol>
<br>
<h2>How to run the project ?</h2>
<ol>
  <li>Clone the project</li>
  <li>Open parking_app.py file</li>
  <li>Run the file</li>
  <li>I have implemented the project so that user can input the data from the terminal using the options provided</li>
</ol>
<br>
<h2> Terminal options when user runs the project</h2>
<ol>
  <li><img width="537" alt="2023-04-27_22h05_37" src="https://user-images.githubusercontent.com/82704862/234930403-cdfc9998-b6a1-4fe0-a9ea-ee21993195a0.png"></li>
  <li><img width="580" alt="2023-04-27_22h06_35" src="https://user-images.githubusercontent.com/82704862/234930625-7daf2a12-c7e2-44f2-b848-c10e129b7042.png"></li>
</ol>
<br>  
<h2>Please feel free to reach out to me for more information</h2>
