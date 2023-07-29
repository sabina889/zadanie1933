import requests

status = "available"

res = requests.put(f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}", data={"accept":"application/json"})

print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))
