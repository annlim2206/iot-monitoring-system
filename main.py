import network
import time
import dht, machine
from umqtt.simple import MQTTClient
import json

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect('DIR-842-2FC3', '1234567890')

while not sta.isconnected():
    time.sleep_ms(300)

print('IP:', sta.ifconfig()[0])

sensor = dht.DHT22(machine.Pin(4))

server = '192.168.0.173'
client_id = 'esp32_sensor'

client = MQTTClient(client_id, server)
client.connect()
print('Connection to MQTT complete.')

topic = b'home/sensor/environment'
while True:
    sensor.measure()
    t = sensor.temperature()
    h = sensor.humidity()
    msg = json.dumps({'temperature': t, 'humidity': h})
    client.publish(topic, msg)
    print('Send in topic', topic, ':', msg)
    time.sleep(5)
