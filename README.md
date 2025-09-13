# Urban Hydroelectric Generator

**Flow-optimised hydroelectric energy generator** designed to harness energy from wastewater in high-rise buildings. Integrates microcontrollers, electromagnets, custom 3D-printed components, and sensors to maximise electricity generation from greywater, with automated redistribution within the pipe network to optimise water head and turbine efficiency.

Extended Project Qualification (**EPQ**) Artefact awarded **100% / A***.

📄 [Download Project Report (PDF)](https://github.com/user-attachments/files/22313024/orlando-alexander-epq-report.pdf)<br><br>


## 🛠 Tech Stack

- **Software:** Python (sensor control, barrier automation, central server coordination), MQTT (real-time commands and data transmission between server and Raspberry Pi microcontrollers)
- **Hardware:** Raspberry Pi microcontrollers, Pelton turbine, electromagnet-operated barriers, liquid level & ultrasonic sensors<br><br>


## 📝 Project Overview

<div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
  <img src="https://user-images.githubusercontent.com/67097862/162108173-7d2c942a-6c5f-4030-97e4-aa91723b43c0.JPG" width="200">
  <img src="https://user-images.githubusercontent.com/67097862/162088634-da5a08fb-c097-48eb-b57a-ca824ceb71d2.jpg" width="200">
  <img src="https://github.com/user-attachments/assets/d746cd39-e799-4a49-b885-92eb0fce0b8c" width="200">
  <img src="https://github.com/user-attachments/assets/691b60f8-c00c-4649-b70d-5aea47d96869" width="200">
</div>
<br>

### How It Works

The generator provides a **compact, localised energy solution** for high-rise buildings, leveraging existing **wastewater infrastructure**. Housed within a **single wastewater pipe** and enclosed in a **3D-printed casing**, it captures the **kinetic energy** of greywater as it passes over a **Pelton turbine** on the ground floor. The system maximizes the energy harnessed from the wastewater by using **Raspberry Pi microcontrollers**, **electromagnet-operated barriers**, and **integrated liquid and ultrasonic sensors** to redistribute the grey wastewater within the pipe. This controlled redistribution enhances the **effective water head**, increasing **power potential** as the water flows across the turbine.

**Dynamic barriers** within the pipe divide the greywater system into sections, with each section corresponding to a specific **floor of the high-rise**. Unlike traditional **water tank-based methods**, which can only harness energy from water above the tank, this system stores wastewater from each floor and directs it across the turbine. Additionally, whereas tank-based systems maintain a constant head, this design retains wastewater close to its original floor height, maximising the **effective water head** and, consequently, the **power potential**, which is an essential factor in **hydropower efficiency**.<br><br>


## 🔧 Software Overview

1. **main.py** – Runs on each Raspberry Pi (located at each pipe barrier mechanism), controlling barrier mechanisms, obtaining sensor readings, and communicating with the central server to coordinate actions.
2. **liquid.py** – Runs on each Raspberry Pi, detecting presence of water below barriers and notifying the central server
3. **server.py** – Coordinates barrier operations based on sensor data and communicates with Raspberry Pi devices via MQTT.  
4. **nodes_sim_main.py / nodes_sim_liquid.py** – Simulates multiple Raspberry Pi devices for testing the entire system.<br><br>



## 📝 Project Components


<img src="https://github.com/user-attachments/assets/965b5094-a5c1-4865-a05c-8b3a7f968ba5" width="1000" />
<img src="https://github.com/user-attachments/assets/1784f18b-e748-42f2-bbe9-5eb645a0122f" width="1000" />
<img src="https://github.com/user-attachments/assets/41511c3b-bad9-4da5-9d30-41cc7dbdf285" width="1000" />
<img src="https://github.com/user-attachments/assets/105b71de-e32c-4812-8369-7add223c9af6" width="1000" />
<img src="https://github.com/user-attachments/assets/8ab40c18-bec1-46ab-bcf4-ceb91275cb6a" width="1000" />
<img src="https://github.com/user-attachments/assets/9533ce99-436e-4ea7-9ac5-1c4edbc365f8" width="1000" />
<img src="https://github.com/user-attachments/assets/0bd9874c-6269-4020-94d5-2b4c76b69e8b" width="1000" />
<img src="https://github.com/user-attachments/assets/58ae23cf-59d3-40b4-8a9c-e0c9ad1c745c" width="1000" />
<img src="https://github.com/user-attachments/assets/69ad6086-1938-4eb0-b7e7-485bbc731c8d" width="1000" />
<img src="https://github.com/user-attachments/assets/f7c23352-b631-4fcb-b77a-5c4e1a812214" width="1000" />
<img src="https://github.com/user-attachments/assets/954566bf-af90-44c8-b47c-68d651d1c2fd" width="1000" />
<img src="https://github.com/user-attachments/assets/7fef541a-206a-48e6-820b-dcf9a8b61fa0" width="1000" />
