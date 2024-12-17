# hindenburg-ground-scanner

## commands
Ros in workspace laden:
source /opt/ros/humble/setup.bash

Ordner erstellen: 
mkdir workspace

In ordnern vor/zurück navigieren:
cd workspace
cd ..

Ein Paket erstellen:
ros2 pkg create uebung3 --build-type ament_python

Im workspace bauen: 
colcon build

Den workspace laden:
source install/setup.bash

Einzelne Node starten:
ros2 run uebung3 pub 

Mit launch-file beide nodes starten:
ros2 launch uebung3 launch.py 

Anzeigen wie ein std_msg String aufgebaut ist:
ros2 interface show std_msgs/msg/String