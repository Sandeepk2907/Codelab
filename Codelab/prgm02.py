import requests
response=requests.get("https://www.google.com")
#print(response.headers)
print(response.status_code)