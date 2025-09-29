# Autopilot suites

In aerial robotics, a UAV’s software stack is typically divided into two subsystems: 

* **The Flight Control Firmware**: embedded onboard the vehicle—manages real-time sensor fusion, attitude stabilization and closed-loop flight control.
* **The Ground Control Station (GCS)**: running on the operator’s workstation—provides the human–machine interface for mission planning, live telemetry monitoring, parameter tuning and post-flight analysis. Below, we list popular open-source flight control firmware and GCS packages along with their supported platforms.

## Flight Control Firmware

Comparison of Flight Control Firmware. [[1]](#references)

| Platform    | Latest Release | OS                       | Language        | License / FC / Doc / Config Tool       |
|-------------|----------------|--------------------------|-----------------|----------------------------------------|
| [Hack flight](https://github.com/simondlevy/Hackflight) | —              | None                     | C++             | GPL-3.0  / – / Lesser GPL-3.0          | |
| [Betaflight](https://github.com/betaflight/betaflight/)  | [v4.5.2](https://github.com/betaflight/betaflight/releases)           | Scheduler                | C               | GPL-3.0  / – / GPL-3.0                 |
| [INAV](https://github.com/iNavFlight/inav/)        | [v8.0.1](https://github.com/iNavFlight/inav/releases)                 | Scheduler                | C               | GPL-3.0  / – / GPL-3.0                 |
| [ArduPilot](https://github.com/ArduPilot/ardupilot/)   | [v4.6.2](https://github.com/ArduPilot/ardupilot/releases)             | ChibiOS / NuttX / Linux  | C/C++           | GPL-3.0  / CC-BY-SA-3.0 / GPL-3.0      |
| [PX4](https://github.com/PX4/PX4-Autopilot/)         | [v1.16.0](https://github.com/PX4/PX4-Autopilot/releases)              | NuttX                    | C/C++           | BSD 2-Clause / CC-BY-SA-3.0 / GPL-3.0  |
| [Paparazzi](https://github.com/paparazzi/paparazzi/)   | [v6.4.0](https://github.com/paparazzi/paparazzi/releases)             | ChibiOS / Scheduler      | C/Python        | GPL-3.0  / GFDL / GPL-3.0              |                    |
| [ROSflight](https://github.com/rosflight/rosflight_firmware/)   | [v1.3.0](https://github.com/rosflight/rosflight_firmware/releases)                    | Linux             | C               | BSD 3-Clause                  |
| [Crazyflie Firmware](https://github.com/bitcraze/crazyflie-firmware/)   | [v2025.09](https://github.com/bitcraze/crazyflie-firmware/releases)          | Linux             | C               | GPL-3.0                       |    


Here is a list of autopilot suites that are either EOL (End of Life) or haven't received an update in the last 5 years:
* [LibrePilot](https://github.com/librepilot/LibrePilot/)
* [dRonin](https://github.com/d-ronin/dRonin/)
* [DJI onboard sdk](https://github.com/dji-sdk/)
* [Cleanflight](https://github.com/cleanflight/cleanflight/)

---

## Ground Control Stations (GCS)

Comparison of GCS software and their supported platforms.[[2]](#references)

| GCS                      | Lastest Release                                                                  | Supported Platforms          | OS (L/W/M)   | Protocol(s)        | Language / Framework   | License                   |
|--------------------------|----------------------------------------------------------------------------------|------------------------------|--------------|--------------------|------------------------|---------------------------|
| Mission Planner          | [v1.3.82](https://github.com/ArduPilot/MissionPlanner/releases)                  | ArduPilot                    | ✕/✓/✓       | MAVLink            | .NET / C#              | GPL-3.0-only              |
| APM Planner 2            | [v2.0.30-rc3](https://github.com/ArduPilot/apm_planner/releases)                 | ArduPilot, PX4               | ✓/✓/✓       | MAVLink            | Qt / C++               | GPL-3.0-or-later          |
| MAVProxy                 | [v1.8.71](https://github.com/ArduPilot/MAVProxy/releases)                        | ArduPilot                    | ✓/✕/✕       | MAVLink            | Python                 | GPL-3.0-or-later          |
| AndroPilot               | [v1.9.14](https://github.com/tstellanova/andropilot/blob/master/RELEASE-NOTES.md)| ArduPilot                    | ✕/✕/✕       | MAVLink            | Java                   | GPL-3.0-only              |
| QGroundControl           | [v4.4.4](https://github.com/mavlink/qgroundcontrol/releases)                     | ArduPilot, PX4               | ✓/✓/✓       | MAVLink            | Qt / C++               | Apache-2.0 / GPL-3.0-only |
| Paparazzi Center         | [v6.4.0](https://github.com/paparazzi/paparazzi/releases)                        | Paparazzi                    | ✓/✓/✓       | PprzLink           | Python                 | GPL-2.0-only              |
| LibrePilot GCS           | [v16.09](https://github.com/librepilot/LibrePilot/tags)                          | LibrePilot                   | ✓/✓/✓       | UAVTalk            | C++ / Qt               | GPL-3.0-only              |
| Betaflight-Configurator  | [v10.10.0](https://github.com/betaflight/betaflight-configurator/releases)       | Betaflight                   | ✓/✓/✓       | MSP, MAVLink       | Electron / JavaScript  | GPL-3.0-only              |
| iNAV-Configurator        | [v8.0.1](https://github.com/iNavFlight/inav-configurator/releases)               | iNAV                         | ✓/✓/✓       | MSP, MAVLink       | Electron / JavaScript  | GPL-3.0-only              |

> **Notes:**  
> - Order for OS is Linux/Windows/macOS, with ✓ = supported, ◐ = partial, ✕ = not supported.
> - AndroPilot is Android-only, hence ✕/✕/✕ here.  
> - All other entries match their official supported OS lists.

---

## References
1. Ebeid, E., Skriver, M., Terkildsen, K.H., Jensen, K. and Schultz, U.P. (2018) A Survey of Open-Source UAV Flight Controllers and Flight Simulators. Microprocessors and Microsystems, 61, 11-20.
[https://doi.org/10.1016/j.micpro.2018.05.002.](https://doi.org/10.1016/j.micpro.2018.05.002)
2. Aliane, N. (2024). A Survey of Open-Source UAV Autopilots. Electronics, 13(23), 4785. [https://doi.org/10.3390/electronics13234785.](https://doi.org/10.3390/electronics13234785)

This page was last updated: *{{ git_revision_date_localized }}*

--8<-- "docs/goatcounter.html"
