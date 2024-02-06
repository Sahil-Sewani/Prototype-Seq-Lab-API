import requests
import json

'''
# GET request to retrieve all employees
response = requests.get('https://seq-lan-api-0f260ca5bb66.herokuapp.com/employees')
if response.status_code == 200:
    employees = response.json()
    for employee in employees:
        print(employee)
else:
    print('Failed to fetch employees')


url = 'https://seq-lan-api-0f260ca5bb66.herokuapp.com/equipment'
data = {
    'name': 'Microscope',
    'model': 'Model X',
    'room_id': 102
}
headers = {'Content-Type': 'application/json'}

# Convert Python dictionary to JSON string
json_data = json.dumps(data)

response = requests.post(url, data=json_data, headers=headers)

if response.status_code == 201:
    print('Equipment added successfully')
else:
    print('Failed to add equipment:', response.status_code)

'''

url = 'https://seq-lan-api-0f260ca5bb66.herokuapp.com/genome/15'

response = requests.get(url)

if response.status_code == 200:
    genome_data = response.json()
    print('Genome ID 15 data:', genome_data)
else:
    print('Failed to retrieve genome ID 15:', response.status_code)


