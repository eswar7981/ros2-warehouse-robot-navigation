# ROS2 Warehouse Robot Navigation



https://github.com/user-attachments/assets/c7e505aa-424f-4a29-899f-f01a92ec93e2



### SLAM Mapping

[▶️ Watch SLAM Mapping Demo](https://drive.google.com/file/d/1JygmbquxjuhONnEBgI136R2PD4LwFgmw/view?usp=sharing)

### Autonomous Navigation

[▶️ Watch Nav2 Autonomous Navigation Demo](https://drive.google.com/file/d/1fvd_cd3SGCED1O3nj5puFycWO63YFhFz/view?usp=sharing)

A simulated warehouse robot built using **ROS 2 Jazzy**, **Gazebo**, **SLAM Toolbox**, **AMCL**, and **Nav2**.

The robot is a differential-drive mobile robot equipped with a LiDAR sensor. The project demonstrates:

- ROS 2 robot description using URDF/Xacro
- Gazebo simulation
- ros2_control differential-drive controller
- LiDAR simulation
- SLAM using SLAM Toolbox
- Map saving and loading
- Localization using AMCL
- Autonomous navigation using Nav2
- RViz visualization
- Waypoint-based navigation

---

## 1. Project Structure

The repository is organized as a ROS 2 workspace:

# ROS2 Warehouse Robot Navigation

A simulated warehouse robot built using **ROS 2 Jazzy**, **Gazebo**, **SLAM Toolbox**, **AMCL**, and **Nav2**.

The robot is a differential-drive mobile robot equipped with a LiDAR sensor. The project demonstrates:

- ROS 2 robot description using URDF/Xacro
- Gazebo simulation
- ros2_control differential-drive controller
- LiDAR simulation
- SLAM using SLAM Toolbox
- Map saving and loading
- Localization using AMCL
- Autonomous navigation using Nav2
- RViz visualization
- Waypoint-based navigation

---

## 1. Project Structure

The repository is organized as a ROS 2 workspace:


ros2-warehouse-robot-navigation/
└── src/
    └── warehouse_robot/
        ├── config/
        ├── launch/
        ├── maps/
        ├── rviz/
        ├── urdf/
        ├── worlds/
        ├── CMakeLists.txt
        └── package.xml

## 2. Requirements

The project was developed using:

Ubuntu 24.04
ROS 2 Jazzy
Gazebo Sim
RViz2

Make sure ROS 2 Jazzy is installed and sourced.

```bash
source /opt/ros/jazzy/setup.bash
```

## 3. Clone the Repository

Clone the repository:
```bash
cd ~
git clone https://github.com/eswar7981/ros2-warehouse-robot-navigation.git
```
Enter the workspace:
```bash
cd ~/ros2-warehouse-robot-navigation
```
The workspace should contain:
```bash
src/
```
Check the package:
```bash
ls src/warehouse_robot
```

## 4. Install Dependencies

From the workspace root:
```bash
cd ~/ros2-warehouse-robot-navigation
```
Run:
```bash
rosdep install --from-paths src --ignore-src -r -y
```
This installs ROS dependencies required by the packages in the workspace.

## 5. Build the Workspace

Source ROS 2:
```bash
source /opt/ros/jazzy/setup.bash
```
Build:
```bash
colcon build --symlink-install
```
After the build completes:
```bash
source install/setup.bash
```
Verify that ROS 2 can find the package:
```bash
ros2 pkg list | grep warehouse_robot
```
Expected output:

warehouse_robot
## 6. Start the Simulation

Launch the warehouse robot simulation:
```bash
ros2 launch warehouse_robot warehouse_bringup.launch.py
```
If the launch file has a different name in your version of the project, check the available launch files with:
```bash
ls src/warehouse_robot/launch
```
Gazebo, RViz, robot_state_publisher and the robot controllers will start.

Note:It may take a few seconds for all ROS 2 nodes, TF frames and controllers to become available.
Initial RViz warnings such as missing TF frames can occur while the nodes are starting.
