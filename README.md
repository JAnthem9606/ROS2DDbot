
# 🤖 diff_drive_bot – ROS 2 Differential Drive Simulation

This ROS 2 package simulates a differential drive robot. It processes velocity commands, converts them into wheel encoder ticks, computes odometry, publishes TF transforms, and visualizes the robot’s path using RViz.

---

## 📁 Package Contents

| File                   | Purpose                                                                 |
|------------------------|-------------------------------------------------------------------------|
| `diff_tf.py`           | Computes odometry and publishes `/odom` and `/tf` using encoder ticks   |
| `twist_to_wheels.py`   | Converts velocity commands (`/cmd_vel`) into left/right encoder ticks    |
| `drive_cmd.py`         | Publishes sample velocity commands using `geometry_msgs/Twist`          |
| `drive_wheels.py`      | Subscribes to `/cmd_vel` and publishes to `/lwheel` and `/rwheel`       |
| `trajectory_publisher.py` | Publishes path traced from odometry to `/robot_path`               |
| `__init__.py`          | Required Python init file for the package                              |

---

## 🧩 ROS 2 Topics Used

- `/cmd_vel` – Velocity commands (`geometry_msgs/Twist`)
- `/lwheel` & `/rwheel` – Wheel encoder ticks (`std_msgs/Int64`)
- `/odom` – Odometry output (`nav_msgs/Odometry`)
- `/tf` & `/tf_static` – Robot transform frames
- `/robot_path` – Path generated from odometry (`nav_msgs/Path`)

---

## ⚙️ How to Run

Make sure your ROS 2 workspace is sourced and the package is built.

```bash
cd ~/ros2_ws
colcon build
source install/setup.bash
```

### Step-by-step Execution

1. **Send velocity commands:**
   ```bash
   ros2 run diff_drive_bot drive_cmd
   ```

2. **Convert `cmd_vel` to wheel encoder ticks:**
   ```bash
   ros2 run diff_drive_bot twist_to_wheels
   ```

3. **Compute odometry from encoder data:**
   ```bash
   ros2 run diff_drive_bot diff_tf
   ```

4. **Publish robot path:**
   ```bash
   ros2 run diff_drive_bot trajectory_publisher
   ```

---

## 🧰 Requirements

- ROS 2 (Foxy, Humble, or later)
- Python 3
- `readchar` Python module (for keyboard input in `drive_cmd.py`)

Install `readchar` if needed:
```bash
pip3 install readchar
```

---

## 📚 Tutorials

Full tutorial with URDF modeling and RViz visualization:  
🔗 [https://github.com/JAnthem9606/ROS-Basics](https://github.com/JAnthem9606/ROS-Basics)

---

## 👨‍💻 Author

Developed by [Bilal Ahmed (JAnthem9606)](https://github.com/JAnthem9606)  
A complete educational ROS 2 robot simulation package.

---

## 📸 Visualization

Launch your URDF in RViz and view real-time TFs and robot path with:
```bash
ros2 launch urdf_tutorial display.launch.py model:=urdf/robot.urdf
ros2 run tf2_tools view_frames
```
