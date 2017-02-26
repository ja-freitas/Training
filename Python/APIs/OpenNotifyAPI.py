import requests, json

# Make a GET request to get the latest position of the international space station

# response = requests.get("http://api.open-notify.org/iss-now.json")
# print("ISS Current Location")
# print(response.status_code)
# print(response.content)

parameters = {"lat": 37.78, "lon": -122.41}

response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# Get the response daata as a python object

data = response.json()
print(type(data))
print(data.content)
