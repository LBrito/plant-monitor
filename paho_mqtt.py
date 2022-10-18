import json
import paho.mqtt.publish as publish

class MQTT: 
    def __init__(self):
        self.__ENDPOINT = "a3cvprzqqgdyma-ats.iot.us-east-1.amazonaws.com"
        self.__PORT = 8883
        self.__TOPIC = "metrics"
    
    def publishMessage(self, message):
        info = publish.single(
            client_id = "metricsReporter",
            hostname = self.__ENDPOINT,
            port = self.__PORT,
            topic = self.__TOPIC,
            payload = json.dumps(message),
            qos = 1,
            tls={
                "ca_certs": "./certs/root-CA.crt",
                "certfile": "./certs/temp_monitor.cert.pem",
                "keyfile": "./certs/temp_monitor.private.key"
                
            })
        print("Successfully published!")
        pass
