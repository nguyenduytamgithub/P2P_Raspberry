#!/usr/bin/python
import sys
import json
import socket                                                                                                          

try:  
		hostname = socket.gethostname().replace('\n','')
		f0=open("/root/.node-red/run/mac.txt", "rb")
		id_mac = f0.read().replace('\n','')  
		with open("/root/.node-red/flows_" + hostname + ".json", "rb") as json_main: 
			json_data = json.load(json_main)
			for item in json_data:
				if item['id'] in ["elefos_mqtt_config"]:
					item['topic'] = id_mac
					print(item['topic'])
				if item['id'] in ["elefos_switch_mac"]:
					item['wires'] = []
				if item['id'] in ["elefos_switch_register"]: 
					item['wires'] = [["elefos_filein_register"]]  
		with open("/root/.node-red/flows_" + hostname + ".json", 'w') as file:
			json.dump(json_data, file, indent=2)
		
except KeyboardInterrupt:
    pass
