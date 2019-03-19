#!/usr/bin/python
import sys
import json

 
try:  
		with open("/root/.node-red/run/ip_broker.json", "rb") as json_broker:
			broker_data = json.load(json_broker)
			id_broker = broker_data['id_server']
			ip_broker = broker_data['ip_server']		   
		with open("/root/.node-red/flows_SuperNode001.json", "rb") as json_main: 
			json_data = json.load(json_main)
			for item in json_data:
				if item['id'] in [id_broker]:
					item['broker'] = ip_broker
					print(item['broker'])  
		with open('/root/.node-red/flows_SuperNode001.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		
except KeyboardInterrupt:
    pass

