import requests
import time
import random

API_KEY = "PDQPI1BGT8PO2N8Y"
URL = "https://api.thingspeak.com/update"

for i in range(5):
    temperature = round(random.uniform(20, 30), 1)
    response = requests.get(URL, params={"api_key": API_KEY, "field1": temperature})
    print(f"Lähetetty: {temperature}, vastaus: {response.text}")
    time.sleep(15)
