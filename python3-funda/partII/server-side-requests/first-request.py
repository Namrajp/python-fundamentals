import requests

# Make an HTTP GET request to a specific URL
r = requests.get('http://omdbapi.com?t=titanic') # returns a response object
print(r.status_code) # 200
print(r.ok) # True
r.headers # see a dictionary of HTTP headers
print(r.json()) # Examine what this data looks like in JSON
