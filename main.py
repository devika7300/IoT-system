import network
import time
import urandom
from umqtt.simple import MQTTClient

class EnvironmentSensor:
    def __init__(self, ssid, password):
        # MQTT credentials and server details
        self.mqtt_client_id = "LCQ7KCIREjYQAR8rITY5PB8"
        self.mqtt_user = "LCQ7KCIREjYQAR8rITY5PB8"
        self.mqtt_password = "u6O3uVfrtlnVpLeFtGvSMULC"
        self.mqtt_server = "mqtt3.thingspeak.com"
        self.mqtt_port = 1883
        self.mqtt_topics = {
            'temperature': "channels/2488614/publish/fields/field1",
            'humidity': "channels/2488614/publish/fields/field2",
            'co2': "channels/2488614/publish/fields/field3",
        }
        # Wi-Fi details
        self.wifi_ssid = ssid
        self.wifi_password = password
        self.historical_data = []
        self.wifi_connect()

    def wifi_connect(self):
        sta_if = network.WLAN(network.STA_IF)
        sta_if.active(True)
        sta_if.connect(self.wifi_ssid, self.wifi_password)
        while not sta_if.isconnected():
            time.sleep(1)
        print("Wi-Fi Connected")

    # Generates random sensor data
    def generate_sensor_data(self):
        return (
            urandom.uniform(-50, 50),  # temperature
            urandom.uniform(0, 100),   # humidity
            urandom.uniform(300, 2000) # CO2
        )

    # Publishes sensor data to ThingSpeak using MQTT
    def publish_to_thingspeak(self, temperature, humidity, co2):
        client = MQTTClient(self.mqtt_client_id, self.mqtt_server, user=self.mqtt_user, password=self.mqtt_password)
        client.connect()
        client.publish(self.mqtt_topics['temperature'], str(temperature))
        client.publish(self.mqtt_topics['humidity'], str(humidity))
        client.publish(self.mqtt_topics['co2'], str(co2))
        client.disconnect()

    def run(self):
        while True:
            data = self.generate_sensor_data()
            self.historical_data.append(data)
            if len(self.historical_data) > 720:
                self.historical_data.pop(0)
            self.publish_to_thingspeak(*data)
            print(f"Published: Temperature={data[0]:.2f}C, Humidity={data[1]:.2f}%, CO2={data[2]:.2f}ppm")
            time.sleep(5)


sensor = EnvironmentSensor("Wokwi-GUEST", "")
sensor.run()
