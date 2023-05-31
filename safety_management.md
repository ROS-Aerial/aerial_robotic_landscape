# Safety and Management Systems

Quadcopter and other Aerial vehicles come in all forms and sizes.
Safety systems are important for all, but the bigger an aerial vehicle becomes, the more important it becomes that the right fail-safes and emergency systems are in place!
This pages gives an overview of those safety systems that have been implemented so far.

## Safety in Autopilot suites
Adapted from the following blogpost: https://www.bitcraze.io/2023/04/safety-and-the-brushless/

These are current Safety managements systems existing in [Paparazzi UAV](https://wiki.paparazziuav.org/wiki/Main_Page), [Betaflight](https://betaflight.com/), [ArduPilot](https://ardupilot.org/) and [PX4](https://px4.io/).
The [Crazyflie ecosystem](https://www.bitcraze.io/) also have some measures but are currently overhauling their safety framework now, so these will be added later.

### Pre-flight checks.

Before a vehicle is allowed to fly, or even before the motors are allowed to spin, which is called ‘arming’, several conditions must be met.
First, it needs to be checked if all internal sensors, such as the IMU, barometer, and magnetometer, are calibrated and functional, so they don’t give values outside of their normal operating range.
Then, the vehicle must receive a GPS signal, and the internal state estimator (usually an extended Kalman filter) should converge to a position based on that information.
It should also be determined if an external remote control is connecting to the vehicle and if there is any datalink to a ground station for telemetry.
Feasibility checks can also be implemented, such as ensuring that the mission loaded to the UAV is not outside its mission parameters or that the start location is not too far away from its take-off position (assuming the EKF is functional).
Additionally, the battery should not be low, and the vehicle should not still be in an error state from a previous flight or crash.

|Preflight check       | PX4 | BET | ARD | PAP |
|----------------------| --- | --- | --- | --- |
|State estimator vs raw| ✓   |     |     |     |
| Internal check est.  | ✓   |     |     |     |
| Raw sensor check     |     |     | ✓   |     |
|  Positioning failures| ✓   |✓   | ✓   |     |


