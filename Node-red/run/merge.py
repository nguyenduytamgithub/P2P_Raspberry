#!/usr/bin/python
import os
import sys
import json
import socket

def insertChar(mystring, position, chartoinsert ):
	#longi = len(mystring)
	mystring   =  mystring[:position] + chartoinsert + mystring[position:] 
	return mystring  
try:  
		hostname = socket.gethostname().replace('\n','')
		f0=open("/root/.node-red/run/id_broker.txt", "rb")
		id_broker = f0.read().replace('\n','')  
		with open("/root/.node-red/flows_" + hostname + ".json", "rb") as json_main: 
			json_data = json.load(json_main)
			for item in json_data:
				if item['id'] in ["elefos_mqtt_request"]:
					item['broker'] = id_broker
					print(item['broker'])
				if item['id'] in ["elefos_mqtt_response"]:
					item['broker'] = id_broker  
		with open("/root/.node-red/flows_" + hostname + ".json", 'w') as file:
			json.dump(json_data, file, indent=2)
		f1=open("/root/.node-red/flows_" + hostname + ".json", "rb") 
		f2=open("/root/.node-red/run/mqtt_broker.json", "rb") 
		f3=open("/root/.node-red/run/flows_raspberrypi2.json","w")
		string1 = f1.read().replace('\n','')
		string2 = f2.read().replace('\n','') 
		length_str1 = len(string1) 
		string_merger = insertChar(string1,length_str1-1,string2)		
		f3.write(string_merger)
		print(length_str1)
		print(len(string_merger))
		os.system('sh /root/.node-red/run/reload.sh')
		
except KeyboardInterrupt:
    pass


