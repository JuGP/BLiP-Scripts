import requests
import uuid
import json

URL = "https://msging.net/commands"

HEADERS_SOURCE = {
	"Authorization": "<put here the authorization key of the source bot's>",
	"Content-Type": "application/json"
}

HEADERS_DESTINATION = {
	"Authorization": "<put here the authorization key of the destination bot's>",
	"Content-Type": "application/json"
}

def GetSourceResources():
	resources = {}
	resourcesKey = GetListOfResources()
	for key in resourcesKey:
		resources[key] = GetResourceValue(key)
	return resources

def GetListOfResources():
	body = {  
		"id": str(uuid.uuid4()),
		"method": "get",
		"uri": "/resources/"
	}
	response = requests.request("POST", URL, headers=HEADERS_SOURCE, data=json.dumps(body))
	resourcesKey = json.loads(response.text)["resource"]["items"]
	return resourcesKey

def GetResourceValue(key):
	body = {  
		"id": str(uuid.uuid4()),
		"method": "get",
		"uri": "/resources/"+key
	}
	response = requests.request("POST", URL, headers=HEADERS_SOURCE, data=json.dumps(body))
	return json.loads(response.text)["resource"]

def SetResourcesOnDestination(resources):
	for key in resources:
		SetResourceValue(key, resources[key])
		print(key+": "+resources[key])

def SetResourceValue(key, value):
	body = {  
		"id": str(uuid.uuid4()),
		"method": "set",
		"uri": "/resources/"+key,
		"type": "text/plain",
		"resource": value
	}
	response = requests.request("POST", URL, headers=HEADERS_DESTINATION, data=json.dumps(body))

resources = GetSourceResources()
SetResourcesOnDestination(resources)
