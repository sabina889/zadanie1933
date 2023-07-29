import requests

status = "available"

res = requests.post(f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}",headers={"accept":"application/json"}, data={"accept":"application/json"})

print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))