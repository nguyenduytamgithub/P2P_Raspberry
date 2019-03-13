#!/usr/bin/python
import sys
import json

 
try:  
		f0=open("/root/.node-red/run/id_broker.txt", "rb")
		id_broker = f0.read().replace('\n','')  
		with open("/root/.node-red/flows_SuperNode002.json", "rb") as json_main: 
			json_data = json.load(json_main)
			for item in json_data:
				if item['id'] in ["elefos_mqtt_request"]:
					item['broker'] = id_broker
					print(item['broker'])
				if item['id'] in ["elefos_mqtt_response"]:
					item['broker'] = id_broker  
		with open('/root/.node-red/flows_SuperNode002.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		
except KeyboardInterrupt:
    pass
