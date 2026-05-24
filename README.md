#  Smart Plant IoT System
# Author: Edel McWilliams

Overview
This project is a simple Internet of Things (IoT) smart plant monitoring system built using a Raspberry Pi and simulated sensor input. The system demonstrates how sensor data can be processed and used to control an actuator (pump) and display results on a web dashboard.

The project follows a layered IoT architecture including sensing (simulation), processing, networking, and application layers.

---------------------

 System Architecture

Sensor Layer: : Sensor values (soil moisture levels) are simulated using HTTP requests sent to the Raspberry Pi server, representing IoT sensor data input.
Network Layer: HTTP protocol is used for communication between components.
Processing Layer: Raspberry Pi runs a Flask-based API that processes incoming sensor values.
Application Layer: A web dashboard displays real-time plant status and actuator state.

-----------------------
How the System Works

1. Sensor values are simulated using Packet Tracer (conceptually)
2. Data is sent via HTTP request to the Raspberry Pi:
3. The Flask server processes the value using threshold logic:
- If value < 20 → Plant needs water
- If value ≥ 20 → Soil is healthy
4. Based on this logic:
- A warning message is generated
- A pump actuator is switched ON or OFF
5. The dashboard updates automatically to show current system status

----------------------------------

Technologies Used

- Python (Flask)
- HTTP REST API
- Raspberry Pi
- Cisco Packet Tracer (conceptual simulation tool)
- HTML (basic web dashboard)

------------------------------

Project Features

- Simulated soil moisture monitoring
- Automated irrigation decision logic
- Real-time dashboard updates
- HTTP communication between devices
- Basic actuator control simulation

----------------------
How to Run the Project

1. Install Flask
bash
pip install -r requirements.txt

2. Start the Flask Server on raspberry pi

bash
python app.py

3. Open the Web Dashboard

http://127.0.0.1:5000
--------------------------

Video Demonstration
https://youtu.be/y2XyCVsNjIM

-------------------------------
Possible future improvements
-Install real soil moisture sensors
-Connect to a physical water pump
-Store the sensor history
-Create mobile phone notifications

