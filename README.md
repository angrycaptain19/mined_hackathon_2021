# mined_hackathon_2021
Realtime Shipment Tracking for MSMEs. Bravo6's submission.

# Project
We intend to create an application which helps MSMEs to track their shipments in realtime as well as provide them with efficient management of their trip data. The project has been implemented in three parts,
- IoT - We aim to tag each truck with an IoT module that captures the locations of these trucks in realtime. For the hackathon we have implemented dummy modules in code which send dummy location values over MQTT.
- Backend Services and Systems - We have a system of microservices interacting with each other, these services responsible for interaction with the front-end apps and with the IoT infrastructures.
- Android Apps - Android apps are used as the interface between the user and our systems.

# Technologies Used
- Python
- Android
- MySQL
- AWS
- Redis

# Libraries Used
- Flask
- Google Maps API
- MQTT
- Volley

# Third Party APIs
- Toll Information Systems, National Highway Authority of India. http://tis.nhai.gov.in/
- Geohacker's Toll Plaza Dataset, https://github.com/geohacker/toll-plazas-india

# Team Info
## Institution
Institute of Technology, Nirma University, Ahmedabad.
## Team Members
- **Krushit Sheth (Team Leader)**
- **Abhi Thakkar**
- **Jainil Patel**
- **Parth Sinha**
- **Vimal Sheoran**

# Code Details
- app/ - Contains code of the backend.
- hackathon.pptx - Presentation of the project.
- gps.py - GPS emulation
- rec.py - Consuming location information from GPS.
- Android Apps - Unable to upload, Google Drive link is provided.
