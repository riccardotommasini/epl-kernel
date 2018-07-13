import requests
import json

import logging

class CEPServer(object):

	def __init__(self, url):
		self.url = url
		self.log = logging.getLogger(__name__)

	#end

	def create_cep(self, name, jdbc=None):
		payload = {}
		payload["cepURI"] = self.url+"/"+name
		if jdbc is not None:
			payload["JDBCConnections"] = jdbc

		response = requests.request("POST", self.url+"/cep", data=json.dumps(payload))
		return response.json()

	#end

	def list_streams(self):
		response = requests.request("GET", self.url+"/streams")
		return response.text
	#end

	def create_stream(self, cep, type_, event_name, schema, connection):
		payload = {}
		payload["cepURI"] = cep
		payload["type"] = type_
		payload["eventName"] = event_name
		payload["dataSchema"] = schema
		payload["connectionInfo"] = connection
		response = requests.request("POST", self.url+"/streams", data=json.dumps(payload))
		return response.json()
	#end

	def list_streams(self):
		response = requests.request("GET", self.url+"/streams")
	#end

	def register_query(self, cep, epl):
		self.log.info(cep + " " + epl)
		payload = {}
		payload["cepURI"]=self.url+"/"+cep
		payload["eplQuery"]=epl
		data = json.dumps(payload)
		self.log.info(data)
		response = requests.request("POST", self.url+"/epl", data=data)
		return response.text

	
	#end

if __name__ == "__main__":
    server = CEPServer("localhost", 3456)
    server.create_cep("brembo")
