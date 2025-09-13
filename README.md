# Urban Hydroelectric Optimisation

<img src="https://user-images.githubusercontent.com/67097862/162108173-7d2c942a-6c5f-4030-97e4-aa91723b43c0.JPG" width="600">

**Compact hydroelectric energy generator** designed to harness energy from wastewater in high-rise buildings. Integrates microcontrollers, electromagnets, and sensors to maximise electricity generation from greywater flow, with automated control of water redistribution and turbine interaction.  

Extended Project Qualification (**EPQ**) Artefact awarded **100% / A***.  

📄 [Download EPQ Report](https://github.com/orlandoalexander/EPQ-Hydroelectric-Generator-for-High-Rise-Buildings/files/8435207/EPQ.Report.Final.docx)<br><br>


## 🛠 Tech Stack

- **Hardware:** Raspberry Pi microcontrollers, Pelton turbine, electromagnet-operated barriers, liquid level & ultrasonic sensors  
- **Software:** Python (sensor control, barrier automation, central server coordination), MQTT (real-time commands and data transmission between server and Raspberry Pi microcontrollers)<br><br>


## 📝 Project Overview

The generator provides a **compact, localised energy solution** for high-rise buildings, leveraging existing wastewater infrastructure. Housed within a single wastewater pipe running along the building, it captures the kinetic energy of greywater as it passes over a Pelton turbine on the ground floor. The system maximizes the energy harnessed from the wastewater by using  Raspberry Pi microcontrollers, electromagnet-operated barriers and integrated liquid and ultrasonic sensors to redistribute the grey wastewater within the pipe. This controlled redistribution enhances the effective water head, increasing power potential as the water flows across the turbine.

### How It Works

Dynamic barriers within the pipe divide the greywater system into sections, with each section corresponding to a specific floor of the high-rise. Unlike traditional water tank-based methods, which can only harness energy from water above the tank, this system stores wastewater from each floor and directs it across the turbine. Additionally, whereas tank-based systems maintain a constant head, this design retains wastewater close to its original floor height, maximising the effective water head and, consequently, the power potential, which is an essential factor in hydropower efficiency.<br><br>


## 🔧 Software Overview

1. **main.py** – Runs on each Raspberry Pi (located at each pipe barrier mechanism), controlling barrier mechanisms, obtaining sensor readings, and communicating with the central server to coordinate actions.
2. **liquid.py** – Runs on each Raspberry Pi, detecting presence of water below barriers and notifying the central server
3. **server.py** – Coordinates barrier operations based on sensor data and communicates with Raspberry Pi devices via MQTT.  
4. **nodes_sim_main.py / nodes_sim_liquid.py** – Simulates multiple Raspberry Pi devices for testing the entire system.<br><br>



## 📝 Project Components


<img src="https://github.com/user-attachments/assets/965b5094-a5c1-4865-a05c-8b3a7f968ba5" width="600" />
<img src="https://github.com/user-attachments/assets/1784f18b-e748-42f2-bbe9-5eb645a0122f" width="600" />
<img src="https://github.com/user-attachments/assets/41511c3b-bad9-4da5-9d30-41cc7dbdf285" width="600" />
<img src="https://github.com/user-attachments/assets/105b71de-e32c-4812-8369-7add223c9af6" width="600" />
<img src="https://github.com/user-attachments/assets/8ab40c18-bec1-46ab-bcf4-ceb91275cb6a" width="600" />
<img src="https://github.com/user-attachments/assets/9533ce99-436e-4ea7-9ac5-1c4edbc365f8" width="600" />
<img src="https://github.com/user-attachments/assets/0bd9874c-6269-4020-94d5-2b4c76b69e8b" width="600" />
<img src="https://github.com/user-attachments/assets/58ae23cf-59d3-40b4-8a9c-e0c9ad1c745c" width="600" />
<img src="https://github.com/user-attachments/assets/69ad6086-1938-4eb0-b7e7-485bbc731c8d" width="600" />
<img src="https://github.com/user-attachments/assets/f7c23352-b631-4fcb-b77a-5c4e1a812214" width="600" />
<img src="https://github.com/user-attachments/assets/954566bf-af90-44c8-b47c-68d651d1c2fd" width="600" />
<img src="https://github.com/user-attachments/assets/7fef541a-206a-48e6-820b-dcf9a8b61fa0" width="600" />








# Hydroelectric Generator for High-Rise Buildings
Concealed system which maximises energy harnessed from wastewater using microcontrollers, electromagnets and sensors.

This project was completed for the Extended Project Qualification (EPQ) and was awarded 100%/A*.

The **hydroelectric generator for high-rise buildings** provides a new, compact energy solution which uses existing infrastructure to generate electricity at a local level. 
The generator system is contained within a single wastewater pipe running down the side of a high-rise building and is powered by 
the kinetic energy of the grey water  as it passes across a Pelton water turbine located on the ground floor of the building. The system maximizes the energy harnessed from the wastewater by using microcontrollers (Raspberry Pi), electromagnet-operated barriers and integrated liquid and ultrasonic sensors which work together to redistribute the grey wastewater throughout the pipe before it is released across the turbine.
<br /><br />
<img src="https://user-images.githubusercontent.com/67097862/162108173-7d2c942a-6c5f-4030-97e4-aa91723b43c0.JPG" align ="left" width="200">
<img src="https://user-images.githubusercontent.com/67097862/162088634-da5a08fb-c097-48eb-b57a-ca824ceb71d2.jpg" align = "left" width="200">
<img src="https://user-images.githubusercontent.com/67097862/162088411-836c58bf-a3d7-4dd9-a7a5-818aa285d646.jpg" align = "center" width="200">
<img src="https://github.com/user-attachments/assets/691b60f8-c00c-4649-b70d-5aea47d96869" align = "center" width="200">



<br />

_Why does this work?_

The use of dynamic barriers within the pipe divide the grey water pipe into sections, with each section corresponding to the piping for one floor in the 
high-rise building. Unlike traditional water tank-based methods of harnessing energy from wastewater which can only capitalise on water leaving the building 
above the tank, this 
system means that the wastewater from each floor in the building is stored and then passed over the turbine. 
Moreover, while water tank-based systems store all the water at a constant head, the wastewater from each floor can be stored at or close to the height at which it is released from the building. 
This greatly increases the power potential from the wastewater, as a key component of hydropower is the water head.


<br />

This repository contains all the programs used within this project:

1. _main.py_ - runs on each Raspberry Pi (located at each pipe barrier mechanism) and executes commands from the central server. These commands include obtaining ultrasonic distance measurements or opening/closing the barrier mechanism.
2. _liquid.py_ - supplementary program which runs on each Raspberry Pi to detect for the presence of water (using the liquid level sensor) below the barrier mechanism, and notifies the central server when water is detected.
3. _server.py_ - coordinates which barrier mechanisms should open and which should close in response to the data it receives from the liquid level and ultrasonic distance sensors connected to each Raspberry Pi. Communciation between the server and the Raspberry Pi devices is using _mqtt_ protocol.
4. _nodes_sim_main.py_ - simulates the behavior of the files _main.py_ which are running on the other Rapsberry Pi devices within the system.
5. _nodes_sim_liquid.py_ - simulates the behavior of the files _liquid.py_ which are running on the other Rapsberry Pi devices within the system.
<br />

<p align="center">
  <img src="https://github.com/user-attachments/assets/cc721d42-e530-41b2-86b4-7c1db2461b9c" width="600" />
  <img src="https://github.com/user-attachments/assets/6569fc2d-6572-49a3-b7ac-77e0a3344ffa" width="600" />
  <img src="https://github.com/user-attachments/assets/50df3fa6-029b-4ac3-bee7-56df596586b1" width="600" />
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/965b5094-a5c1-4865-a05c-8b3a7f968ba5" width="600" />
  <img src="https://github.com/user-attachments/assets/1784f18b-e748-42f2-bbe9-5eb645a0122f" width="600" />
  <img src="https://github.com/user-attachments/assets/41511c3b-bad9-4da5-9d30-41cc7dbdf285" width="600" />
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/105b71de-e32c-4812-8369-7add223c9af6" width="600" />
  <img src="https://github.com/user-attachments/assets/8ab40c18-bec1-46ab-bcf4-ceb91275cb6a" width="600" />
  <img src="https://github.com/user-attachments/assets/9533ce99-436e-4ea7-9ac5-1c4edbc365f8" width="600" />
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/0bd9874c-6269-4020-94d5-2b4c76b69e8b" width="600" />
  <img src="https://github.com/user-attachments/assets/58ae23cf-59d3-40b4-8a9c-e0c9ad1c745c" width="600" />
  <img src="https://github.com/user-attachments/assets/69ad6086-1938-4eb0-b7e7-485bbc731c8d" width="600" />
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/f7c23352-b631-4fcb-b77a-5c4e1a812214" width="600" />
  <img src="https://github.com/user-attachments/assets/954566bf-af90-44c8-b47c-68d651d1c2fd" width="600" />
  <img src="https://github.com/user-attachments/assets/7fef541a-206a-48e6-820b-dcf9a8b61fa0" width="600" />
</p>
 
<br/>

Feel free to have a read of my report on the project if you have a moment (or a few!). It covers the background to the project, the development process and all the nitty-gritty design details:

[EPQ Report.docx](https://github.com/orlandoalexander/EPQ-Hydroelectric-Generator-for-High-Rise-Buildings/files/8435207/EPQ.Report.Final.docx)


