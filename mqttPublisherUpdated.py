#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random, uuid, signal
import time, sys
from time import sleep
from socket import gethostname
from paho.mqtt import client as mqtt_client
from urllib.parse import urlencode
from urllib.request import Request, urlopen

def sigterm_handler(_signo, _stack_frame):
    # Raises SystemExit(0):
    sys.exit(0)

if sys.argv[1] == "handle_signal":
    signal.signal(signal.SIGTERM, sigterm_handler)

broker = '172.31.5.135'
port = 1884
topic = "/smartMeter/birectionalTopic"

def getContainerName():
    return str(gethostname())

def getDeviceName(containerName):
    url = 'http://172.31.5.135:5001/insert' # Set destination URL here
    post_fields = {'containerName': containerName}     # Set POST fields here
    request = Request(url, urlencode(post_fields).encode())
    deviceName = urlopen(request).read().decode()
    return str(deviceName)

def removeDeviceFromRegistry(deviceName):
    url = 'http://172.31.5.135:5001/delete/'+deviceName # Set destination URL here
    #post_fields = {'containerName': containerName+str(12345)}     # Set POST fields here
    request = Request(url,method='DELETE')
    reponse = urlopen(request,timeout=10)
    return str("Device Deleted "+deviceName)

client_id = getDeviceName(getContainerName()) #str(uuid.uuid1())
print(client_id)

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client,msg):
    msg_count = 0
    result = client.publish(topic, msg)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")
    msg_count += 1

def main():
    client = connect_mqtt()
    try:
        while True:
            publish(client,msg="Connected to MQTT Broker : Vivek")
            sleep(1)
    finally:
        print("Disconnecting from Mqtt")
        print(removeDeviceFromRegistry(client_id))
    
# In[ ]:

main()

# In[ ]:




