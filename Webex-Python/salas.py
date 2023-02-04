import requests

url = "https://webexapis.com/v1/rooms"

payload = "{\"title\":\"Actividad J,A,C\"}"
headers = {
    'user-agent': "vscode-restclient",
    'content-type': "application/json",
    'authorization': "Bearer OTliNTc3OTYtNTczZC00MDI5LTlmMDAtOTQ1YjRhYTgwNmEyODBkZWM0YWUtOTQ3_P0A1_ff79c397-9d79-44f7-8296-8858b58f5ba8"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
