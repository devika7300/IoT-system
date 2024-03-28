# IoT-system

## Description

This project develops a cloud-based IoT system for capturing data from virtual sensors, aiming to collect environmental information such as temperature, humidity, and CO2 levels. The system is designed to demonstrate the capabilities of IoT technologies in monitoring environmental conditions through the use of virtual sensors and cloud platforms.

## Features

- **Virtual Sensor Simulation**: Utilizes Wokwi to simulate an environmental IoT station, generating random values for temperature, humidity, and CO2 sensors.
- **Unique Station Identification**: Each virtual environmental station operates with a unique ID, facilitating the publishing of sensor data to an MQTT channel.
- **Cloud-based IoT Backend**: Leverages ThingSpeak as the cloud platform to manage the MQTT protocol for communication, storage, and processing of sensor data.
- **Data Visualization**: Employs ThingSpeak's visualization tools to display the latest sensor data from all sensors of a specified environmental station, and the sensor data received over the last five hours for a specified sensor.

## Requirements

- **Wokwi**: An online simulator for IoT and embedded systems, used for creating the virtual sensors and environmental stations.
- **ThingSpeak**: A cloud service for IoT applications, providing capabilities for data collection, processing, and visualization.

## Implementation Steps

### Step 1: Simulation Setup with Wokwi
- Designed and configured virtual sensors within Wokwi to simulate temperature, humidity, and CO2 measurements, ensuring each virtual environmental station could generate and publish random sensor data.

### Step 2: MQTT Configuration for ThingSpeak
- Set up the MQTT broker provided by ThingSpeak, configuring virtual stations to publish their data to ThingSpeak channels using unique IDs for each station.

### Step 3: ThingSpeak Cloud Backend Setup
- Configured ThingSpeak channels to receive data from the MQTT broker, setting up necessary fields for temperature, humidity, and CO2 sensor data.
- Utilized ThingSpeak's built-in MQTT API for seamless data transmission and storage.

### Step 4: Visualization and Data Display
- Implemented scripts to utilize ThingSpeak's visualization tools, displaying the latest sensor data from all sensors for a specified station, and historical data for a specified sensor from the last five hours.
