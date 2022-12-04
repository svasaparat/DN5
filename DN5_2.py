import requests


data = requests.get("https://jsonplaceholder.typicode.com/todos/1")

if data.status_code == 200:
    print(data.json())
else:
    print("False")





