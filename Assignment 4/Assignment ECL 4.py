import time
import board
import adafruit_dht
import paho.mqtt.client as mqtt

dht_device = adafruit_dht.DHT11(board.D4)  # GPIO Pin 4

# MQTT Broker Details
MQTT_BROKER = "localhost"  # or Raspberry Pi's IP
MQTT_PORT = 1883
MQTT_TOPIC = "sensor/dht11"

# MQTT Client Setup
client = mqtt.Client("RPi_Publisher")
client.connect(MQTT_BROKER, MQTT_PORT)

try:
    while True:
        try:
            temperature = dht_device.temperature
            humidity = dht_device.humidity
            
            payload = f"Temperature: {temperature}°C, Humidity: {humidity}%"
            client.publish(MQTT_TOPIC, payload)
            print(f"Published: {payload}")
            
        except RuntimeError as e:
            print(f"Error reading DHT11: {e}")
        
        time.sleep(2)  # Publish every 2 seconds

except KeyboardInterrupt:
    print("Exiting...")
    client.disconnect()
