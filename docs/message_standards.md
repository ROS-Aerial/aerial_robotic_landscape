# Message standards

## REP 147 A Standard interface for Aerial Vehicles

Within the ROS ecoysystem, there is currently a ROS enhancement proposal (REP) available to give guidance to message standards for UAVS. This can be found here:

[REP 147 A Standard interface for Aerial Vehicles](https://www.ros.org/reps/rep-0147.html)

## Message standards within autopilot suites

### MAVlink

MAVLink, an acronym for Micro Air Vehicle Link, is a communication system mainly used for the exchange of information between unmanned aerial vehicles and ground control stations.
This protocol, which was launched in 2009, is structured as a header-only message marshaling library.
MAVLink is versatile, supporting a broad range of messages and capable of being sent over virtually any type of serial connection, including Wi-Fi and radio technologies.
In terms of messages, they are defined at compile time in XML files, which are processed to create libraries for sending and receiving messages.
If new messages are added or existing ones are modified, the XML definitions need to be updated and the application recompiled.

https://mavlink.io/en/

MAVlink is used in 2 autopilot suites. Eventhough the same message type are being shared in both the suites, the accomendating behavior might differ:

* [Ardupilot MAVlink usage](https://ardupilot.org/dev/docs/mavlink-basics.html)
* [PX4 MAVlink usage](https://docs.px4.io/main/en/middleware/mavlink.html)

--8<-- "docs/goatcounter.html"

