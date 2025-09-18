import network 
import time         
import urequests  
import dht           
from machine import Pin  

ssid = 'YOUR_WIFI_SSID'     
password = 'YOUR_WIFI_PASSWORD'

THINGSPEAK_API_KEY = 'YOUR_WRITE_API_KEY'
THINGSPEAK_URL = 'https://api.thingspeak.com/update' 

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

print("Connecting to Wi-Fi...", end="")
while not wlan.isconnected():
    print(".", end="")
    time.sleep(0.5)

print("\nConnected!")
print("IP address:", wlan.ifconfig()[0])

sensor = dht.DHT22(Pin(15))


led = Pin(25, Pin.OUT)

def send_to_thingspeak(temp, hum):
    if temp is None or hum is None:
        print("No data to send.")
        return
    try:
        data = 'api_key={}&field1={}&field2={}'.format(THINGSPEAK_API_KEY, temp, hum)
        response = urequests.post(
            THINGSPEAK_URL,
            data=data,
            headers={'Content-Type': 'application/x-www-form-urlencoded'}
        )
        print("ThingSpeak response:", response.text)
        response.close()
    except Exception as e:
        print("Failed to send data:", e)

while True:
    try:
        sensor.measure()
        temperature = sensor.temperature()
        humidity = sensor.humidity()
        print("Temperature: {:.1f} °C".format(temperature))
        print("Humidity: {:.1f}%".format(humidity))

        send_to_thingspeak(temperature, humidity)
    except OSError as e:
        print("Sensor read error:", e)
    except Exception as e:
        print("Error sending data:", e)

    time.sleep(15)
