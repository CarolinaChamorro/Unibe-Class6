import requests

url = "https://webexapis.com/v1/messages"

payload = "{\"roomId\":\"Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vMTc3YzZhYzAtOTk5NS0xMWVkLWIwNWItMjllOTFmZjM2YWQ0\",\"text\":\"Mensaje\",\"markdown\":\"Hola desde python Firma: Angie :3\"}"
headers = {
    'user-agent': "vscode-restclient",
    'content-type': "application/json",
    'authorization': "Bearer ZjU1ZGU0ZmEtZDU5Ny00NjJjLTk2ZWMtYmQ4MGM0NjhiZmQ3NjQ3YzM4NDMtMTdm_P0A1_023934c2-3934-48f9-b7e3-18314460f059"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
