# Hydroelectric Generator for High-Rise Buildings
Concealed system which maximises energy harnessed from wastewater using microcontrollers, electromagnets and sensors.

This project was completed for the Extended Project Qualification (EPQ) and was awarded 100%/A*.

My **hydroelectric generator for high-rise buildings** provides a new, compact energy solution which uses existing infrastructure to generate electricity at a local level. 
The generator system is contained within a single wastewater pipe running down the side of a high-rise building and is powered by 
the kinetic energy of the grey water  as it passes across a Pelton water turbine located on the ground floor of the building. The system maximizes the energy harnessed from the wastewater by using microcontrollers (Raspberry Pi), electromagnet-operated barriers and integrated liquid and ultrasonic sensors which work together to redistribute the grey wastewater throughout the pipe before it is released across the turbine.
<br /><br />
<img src="https://user-images.githubusercontent.com/67097862/162108173-7d2c942a-6c5f-4030-97e4-aa91723b43c0.JPG" align ="left" width="200">
<img src="https://user-images.githubusercontent.com/67097862/162088634-da5a08fb-c097-48eb-b57a-ca824ceb71d2.jpg" align = "left" width="200">
<img src="https://user-images.githubusercontent.com/67097862/162088411-836c58bf-a3d7-4dd9-a7a5-818aa285d646.jpg" align = "center" width="200">




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

Feel free to have a read of my report on the project, if you have a moment(!). It covers the background to the project, the development process and all the nitty-gritty design details:

[EPQ Report.docx](https://github.com/orlandoalexander/EPQ-Hydroelectric-Generator-for-High-Rise-Buildings/files/8435207/EPQ.Report.Final.docx)


