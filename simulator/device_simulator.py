import paho.mqtt.client as mqtt
import time

BROKER_HOST = "localhost"
BROKER_PORT = 1883

def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected to broker, result code: {reason_code}")

def main():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_connect = on_connect

    client.connect(BROKER_HOST, BROKER_PORT, keepalive=60)
    client.loop_start()

    time.sleep(2)
    client.loop_stop()
    client.disconnect()

if __name__ == "__main__":
    main()