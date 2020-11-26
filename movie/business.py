import requests
import json     
response = requests.get("http://www.omdbapi.com/?t=The Wolf of Wall Street&apikey=198361c3")
print(response.status_code)
#print(response.json())
data = json.loads(response.text)       
print (data)