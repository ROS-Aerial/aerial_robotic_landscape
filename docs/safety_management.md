# Safety and Management Systems

Quadcopter and other Aerial vehicles come in all forms and sizes.
Safety systems are important for all, but the bigger an aerial vehicle becomes, the more important it becomes that the right fail-safes and emergency systems are in place!
This pages gives an overview of those safety systems that have been implemented so far.

## Safety in ROS

Currently specifically for aerial vehicles, the safety implementation is depended on the [ROS autonomy stack]((aerial_autonomy_stacks.md) used. 

The [ROS-0147](https://ros.org/reps/rep-0147.html) has a suggestion for flightmodes for a statemachine that can simplify the understanding of it. It is also expecting that ROS will be run offboard on an external computer, and that it should be in control of the safety state machine. This should probably be discussed if it would be a good idea for ROS to be in control of this or the autopilot suites themselves.

## Safety in Autopilot suites
Adapted from the following blogpost: https://www.bitcraze.io/2023/04/safety-and-the-brushless/

These are current Safety managements systems existing in [Paparazzi UAV](https://wiki.paparazziuav.org/wiki/Main_Page), [Betaflight](https://betaflight.com/), [ArduPilot](https://ardupilot.org/) and [PX4](https://px4.io/).
The [Crazyflie ecosystem](https://www.bitcraze.io/) also have some measures but are currently overhauling their safety framework now in the form of a supervisor.

### Pre-flight checks.

Before a vehicle can fly, certain conditions must be met. These includ:

* calibrating and ensuring functionality of internal sensors (IMU, barometer, magnetometer)
*  receiving a GPS signal
*  converging the internal state estimator (usually an extended Kalman filter) to a position
*  checking for remote control connection and datalink to a ground station
*  conducting feasibility checks (e.g., mission parameters, start location proximity)
*  confirming sufficient battery level, and ensuring the absence of error states from previous flights or crashes.

**Preflight checks documentation:**

* PX4: https://docs.px4.io/main/en/flying/pre_flight_checks.html#preflight-sensor-estimator-checks
* ArduPilot: https://ardupilot.org/copter/docs/common-prearm-safety-checks.html#failure-messages
* Beta flight: https://betaflight.com/docs/wiki/archive/GPS-Rescue-v4-4#sanity-check-options
* Paparazzi UAV: Indicated per platform if necessary, on their wiki:  https://wiki.paparazziuav.org/wiki/Failsafe
* Crazyflie firmware: https://www.bitcraze.io/documentation/repository/crazyflie-firmware/master/functional-areas/supervisor/

### Fail-safe mechanisms

After passing pre-flight checks and arming the UAV, the takeoff command is given. However, UAV flights have inherent risks, particularly during takeoff. To mitigate these risks, numerous safety features, known as failsafes, are implemented during the flight phase. These failsafes are categorized as triggers and behaviors, allowing developers to specify the UAV's response to different failures, such as initiating a safe landing in the event of GPS loss.

#### Triggers
Thus, there are triggers that can enable the autopilot’s failsafe mechanics:

* No connection with the remote control
* No connection with the Ground station or Datalink
* Low Battery
* Position estimate diverges or full GPS loss
* Waypoint going beyond geofence or Mission is not feasible
* Other vehicles are nearby.

Also, sometimes the support of an external Automatic Trigger system is required, which is a box that monitors the conditions where the UAV should take action in case there is no GPS, other aerial vehicles are nearby, or the UAV is crossing a geofence determined by outdoor flight restrictions. Note that all of these triggers usually have a couple of conditions attached, such as the level of the ‘low battery’ or the number of seconds of ‘GPS loss’ deemed acceptable.

#### Fail-safe behaviors

During UAV flights, safety features can be customized per trigger, deviating from the default actions set by regulations. Disarming the vehicle completely increases the risk of crashing and causing harm. Allowing the drone to autonomously complete the mission without intervention poses the risk of losing the vehicle or trespassing restricted areas. Modifying default behaviors should be undertaken by knowledgeable individuals with careful consideration.

These behaviors can include the following:

* No action at all
* Warning on the console or remote control display
* Continue the mission autonomously
* Stay still at the same position or go to a home position
* Fly to a lower altitude
* Land based on position or safely land by reducing thrust
* No input to motors or completely disarming the motors

**Fail-safe documentation**
* PX4: https://docs.px4.io/main/en/config/safety.html
* ArduPilot: https://ardupilot.org/copter/docs/failsafe-landing-page.html
* Betaflight: https://betaflight.com/docs/development/Failsafe
* Paparazzi UAV: https://wiki.paparazziuav.org/wiki/Failsafe
* Crazyflie firmware: https://www.bitcraze.io/documentation/repository/crazyflie-firmware/master/functional-areas/supervisor/


### Emergencies

Fail-safes ensure safe flight, but emergencies like crashes, flips, or hardware failures can still occur. In such cases, the standard default action is to disarm the vehicle to prevent unintended motor activation. Backup systems connected to ESCs may take over if the autopilot becomes unresponsive. The pilot plays a vital role in safety, with the remote control featuring a dedicated button or switch for different modes, enabling actions like landing or disarming. It's recommended to have a net or towel to stop spinning motors and to promptly disconnect the battery. Being prepared for potential LiPo battery hazards is essential, with sand or fire retardant on hand. While autopilots provide guidance, conducting thorough research on handling emergencies, spinning parts, and LiPo battery fires is crucial.

Here a list of that:
* Remote control should have a dedicated button/switch for different modes, landing, or disarming.
* Dealing with spinning motors Use a net or towel to stop them and promptly disconnect the battery.
* To prepare for LiPo battery hazards, Have sand or fire retardant available.
