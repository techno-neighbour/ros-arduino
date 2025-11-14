# 🤖 Robotics & Embedded Systems Projects

This repository contains a collection of Arduino, PySerial, and ROS2 projects built during my robotics learning journey.
Each project focuses on system behaviour, real-world actuation, sensor interaction, and ROS2 node communication.

You will find:

• Microcontroller-based circuits

• Python–Arduino serial communication

• ROS2 packages (Python and C++)

• Modular nodes for sensing, actuation, and data flow

• Hardware-software integrated experiments

This repo is structured to keep Arduino and ROS2 work separate while allowing cross-integration through PySerial and custom ROS2 nodes.

---

## 📁 File Structure
    ├── arduino/
    │   ├── Normal projects/          # Basic Arduino circuits and logic
    │   └── Pyserial projects/        # Arduino sending data to Python
    │
    ├── ros2_ws/
        └── src/
            ├── bu_files/             # Bringup-related C++ files or packages
            ├── in_files/             # Interfaces/message definitions
            └── py_files/             # Python ROS2 package
                ├── py_files/
                │   ├── normal/       # Standard ROS2 Python nodes
                │   └── pyserial/     # Python nodes using PySerial (Robot, simple demos)
                │       ├── car/
                │       └── simple/
                ├── resource/
                ├── test/
                ├── package.xml
                ├── setup.cfg
                └── setup.py

    ├── LICENSE
    └── readme.md         # This file

---

## 🗂️ Project Index
### Arduino Projects 
#### • [Normal Arduino Projects](arduino/Normal%20projects/) 
#### • [PySerial-Based](arduino/Pyserial%20projects/)

### ROS2 Projects 
#### • [Bringup Files](ros2_ws/src/bu_files/) 
#### • [Interface Files](ros2_ws/src/in_files/) 
#### • Python ROS2 Package

#####   └── [Normal Python Nodes](ros2_ws/src/py_files/py_files/normal/)
#####   └──  [PySerial-Based Nodes](ros2_ws/src/py_files/py_files/pyserial/)

---

## ⚙️ Requirements 
• VSCode

• ROS2

• Arduino IDE

• Arduino UNO

---

## ▶️ How to Run the Projects
### Arduino
#### Normal Arduino

1. Open the .ino file in Arduino IDE.

2. Select board and port.

3. Upload.

#### PySerial Arduino

1. Upload the .ino program to y.

2. Install PySerial with:

````cmd
pip install pyserial
````

3. Run Python script:

````cmd
python3 script.py
````

Or run the Python script using VSCode.

### ROS2
First, we have to build our workspace

````cmd
cd ros2_ws
colcon build
source install/setup.bash
````

• Run Python Nodes

````cmd
source install/setup.bash
ros2 run <package> <executable>
````

• Run Launch files

````cmd
source install/setup.bash
ros2 launch py_files <launch_file>.launch.py
````

---

## 👥 Contributing 

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Make sure to update tests as appropriate.

---

## 📄   License 
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
