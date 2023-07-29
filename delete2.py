import requests

status = "available"

res = requests.delete(f"https://petstore.swagger.io/v2/swagger.json/findByStatus?status={status}", **kwargs ={"accept":"application/json"})

print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))