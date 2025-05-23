
# 🛸 Autonomous Drone Project

## 🚀 Deployment Instructions

### 🧰 Hardware Requirements

1. **Pixhawk Flight Controller** (e.g., Pixhawk 4, Cube Orange)  
2. **Raspberry Pi 4** (or Jetson Nano for better CV performance)  
3. **GPS Module** (e.g., Ublox NEO-M8N)  
4. **Telemetry Radio (915 MHz or 433 MHz)**  
5. **Onboard Camera** (e.g., Pi Camera or USB webcam)  
6. **Micro SD Card (32GB or higher)**  
7. **Power Module + ESCs + Motors + Frame**  
8. **Onboard Speaker** (for survivor alert)  
9. **Servo or Relay-Based Payload Dropper**  
10. **Battery (3S or 4S LiPo)**  

### ⚙️ Software Stack

- Raspberry Pi OS (Lite or Full)  
- Python 3.x  
- MAVProxy / DroneKit-Python  
- Flask (for web dashboard)  
- OpenCV & YOLOv5 for object detection  
- Pyserial, requests, numpy, pandas, etc.  

## 🔧 Raspberry Pi Setup

### 1. Flash and Boot OS

- Use [Raspberry Pi Imager](https://www.raspberrypi.com/software/) to flash Raspberry Pi OS.  
- Enable SSH and Wi-Fi from boot (`/boot/ssh` & `wpa_supplicant.conf`).  
- Boot up and SSH into Pi.  

### 2. Install Dependencies

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-opencv python3-flask git -y
pip3 install dronekit pymavlink opencv-python flask pandas numpy
```

### 3. Enable Serial Port for MAVLink

```bash
sudo raspi-config
# → Interface Options → Serial → No shell, Enable serial port
```

Disable console from `/boot/cmdline.txt`:

```bash
sudo nano /boot/cmdline.txt
# REMOVE: console=serial0,115200
```

Reboot:

```bash
sudo reboot
```

### 4. Connect Pixhawk to Pi via UART or USB

- UART: Use `/dev/serial0`  
- USB: Use `/dev/ttyACM0`  

### 5. Clone Project and Set Permissions

```bash
git clone https://github.com/YOUR-REPO/Autonomous-Drone.git
cd Autonomous-Drone
chmod +x mission_start.py
```

### 6. Upload KML File for Waypoints

Save your `.kml` file in the project root as `mission.kml`.

### 7. Launch the Mission

```bash
python3 mission_start.py
```

## 📺 Dashboard Setup

### 1. Start Flask Web UI

```bash
python3 app.py
```

Open in browser: `http://<your-pi-ip>:5000`

### 2. Dashboard Features

- Live telemetry (GPS, battery, state)  
- Map with survivor locations  
- Drop zone tracking  
- Mission log viewer  

## 🧪 Testing & Simulation (Optional)

Use **SITL (Software In The Loop)**:

```bash
pip install MAVProxy
sim_vehicle.py -v ArduCopter -f quad --console --map
```

Run your project code using `--connect 127.0.0.1:14550`.

## 🛑 Safety Checklist

- Calibrate compass, GPS, ESCs before deployment  
- Configure failsafe in Mission Planner/QGroundControl  
- Check propeller direction and motor order  
- Fully charge battery before flight  
- Keep fire extinguisher nearby (LiPo safety)  
