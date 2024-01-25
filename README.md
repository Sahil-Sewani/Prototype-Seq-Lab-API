# Seq-Lab-API

#### Base URL: https://seq-lan-api-0f260ca5bb66.herokuapp.com/

*This applicaiton does not require a local host to run, copy-paste the link above in web browser and use the same endpoints listed in the README*

### Running the API Locally

Alternatively, you can run the API code on your local machine by cloning this repository and executing the API code provided in the repository.

Ensure you have the required dependencies installed, then execute the API code. By default, the API may run on `http://localhost:5000` or another specified port.

Once the API is running locally, you can use the following URLs for accessing the endpoints:
- Retrieve all employees: `GET http://localhost:5000/employees`
- Retrieve a all genomes: `GET http://localhost:5000/genome`

#### To interact with these endpoints, you can use tools like Postman to make HTTP requests.

## Employee Routes

### Get All Employees

- **Route:** `GET /employees`
- **Description:** Retrieves details of all employees.
- **Response:** Returns a JSON array containing employee details.

### Get Employee by ID

- **Route:** `GET /employees/{employee_id}`
- **Description:** Retrieves details of a specific employee by ID.
- **Response:** Returns JSON data for the employee or a 404 error if not found.

### Add Employee

- **Route:** `POST /employees`
- **Description:** Adds a new employee to the database.
- **Request Body:** JSON object with keys: `employee_id`, `employee_name`, `employee_role`, `employee_clearance_level`.
- **Response:** Indicates successful addition or an error.

### Update Employee

- **Route:** `PUT /employees/{employee_id}`
- **Description:** Updates details of an existing employee.
- **Request Body:** JSON object with keys: `employee_name`, `employee_role`, `employee_clearance_level`.
- **Response:** Indicates successful update or an error.

### Delete Employee

- **Route:** `DELETE /employees/{employee_id}`
- **Description:** Deletes an employee by ID.
- **Response:** Indicates successful deletion or an error.

## Consumable Routes

### Get All Consumables

- **Route:** `GET /consumables`
- **Description:** Retrieves details of all consumables.
- **Response:** Returns a JSON array containing consumable details.

### Get Consumable by ID

- **Route:** `GET /consumables/{consumable_id}`
- **Description:** Retrieves details of a specific consumable by ID.
- **Response:** Returns JSON data for the consumable or a 404 error if not found.

### Add Consumable

- **Route:** `POST /consumables`
- **Description:** Adds a new consumable to the database.
- **Request Body:** JSON object with keys: `consumable_name`, `quantity`, `room_id`.
- **Response:** Indicates successful addition or an error.

### Update Consumable

- **Route:** `PUT /consumables/{consumable_id}`
- **Description:** Updates details of an existing consumable.
- **Request Body:** JSON object with keys: `consumable_name`, `quantity`, `room_id`.
- **Response:** Indicates successful update or an error.

### Delete Consumable

- **Route:** `DELETE /consumables/{consumable_id}`
- **Description:** Deletes a consumable by ID.
- **Response:** Indicates successful deletion or an error.

## Equipment Routes

### Get All Equipment

- **Route:** `GET /equipment`
- **Description:** Retrieves details of all equipment.
- **Response:** Returns a JSON array containing equipment details.

## Genome Routes

### Get All Genome Entries

- **Route:** `GET /genome`
- **Description:** Retrieves details of all genome entries.
- **Response:** Returns a JSON array containing genome details.

### Get Genome Entry by ID

- **Route:** `GET /genome/{genome_id}`
- **Description:** Retrieves details of a specific genome entry by ID.
- **Response:** Returns JSON data for the genome entry or a 404 error if not found.

### Add Genome Entry

- **Route:** `POST /genome`
- **Description:** Adds a new genome entry to the database.
- **Request Body:** JSON object with keys: `equipment_id`, `type`, `species_name`, `the_sequence`.
- **Response:** Indicates successful addition or an error.

### Update Genome Entry

- **Route:** `PUT /genome/{genome_id}`
- **Description:** Updates details of an existing genome entry.
- **Request Body:** JSON object with keys: `equipment_id`, `type`, `species_name`, `the_sequence`.
- **Response:** Indicates successful update or an error.

### Delete Genome Entry

- **Route:** `DELETE /genome/{genome_id}`
- **Description:** Deletes a genome entry by ID.
- **Response:** Indicates successful deletion or an error.

## Room Routes

### Get All Rooms

- **Route:** `GET /rooms`
- **Description:** Retrieves details of all rooms.
- **Response:** Returns a JSON array containing room details.

### Get Room by Number

- **Route:** `GET /rooms/{room_number}`
- **Description:** Retrieves details of a specific room by number.
- **Response:** Returns JSON data for the room or a 404 error if not found.

### Add Room

- **Route:** `POST /rooms`
- **Description:** Adds a new room to the database.
- **Request Body:** JSON object with keys: `room_number`, `room_description` (optional), `room_type` (optional).
- **Response:** Indicates successful addition or an error.

### Update Room

- **Route:** `PUT /rooms/{room_number}`
- **Description:** Updates details of an existing room.
- **Request Body:** JSON object with keys: `room_description` (optional), `room_type` (optional).
- **Response:** Indicates successful update or an error.

### Delete Room

- **Route:** `DELETE /rooms/{room_number}`
- **Description:** Deletes a room by number.
- **Response:** Indicates successful deletion or an error.

## How to Use

1. **Endpoints**: Utilize the respective HTTP methods (`GET`, `POST`, `PUT`, `DELETE`) along with the provided endpoints appended to the base URL to interact with the database tables.
2. **Database Configuration**: No local configuration needed; the API is hosted at the specified base URL.

The API provides endpoints to interact with the database tables. You can interact with the API using code, through a web browser, or via HTTP services like Postman.

### Using Code (Python Example)

You can utilize the API endpoints using Python and the `requests` library. Here are a few examples demonstrating how to interact with the API:

### Examples of API usage
#### Viewing all employees

```{python}
import requests

base_url = "https://seq-lan-api-0f260ca5bb66.herokuapp.com/"
employees_endpoint = base_url + "employees"

response = requests.get(employees_endpoint)

if response.status_code == 200:
    employees = response.json()
    print("All Employees:")
    for employee in employees:
        print(employee)
else:
    print("Failed to retrieve employees. Status code:", response.status_code)

```

#### Adding a new equipment
```{python}
import requests

base_url = "https://seq-lan-api-0f260ca5bb66.herokuapp.com/"
equipment_endpoint = base_url + "equipment"

new_equipment = {
    "name": "Sequencer XYZ",
    "model": "Model ABC",
    "room_id": 310  # Replace with an existing room ID
}

response = requests.post(equipment_endpoint, json=new_equipment)

if response.status_code == 201:
    print("New equipment added successfully!")
else:
    print("Failed to add equipment. Status code:", response.status_code)
```

#### Updating employee's information
```{python}
import requests

base_url = "https://seq-lan-api-0f260ca5bb66.herokuapp.com/"
employee_id = 5  # Replace with an existing employee ID
employee_endpoint = f"{base_url}employees/{employee_id}"

updated_info = {
    "employee_name": "Updated Name",
    "employee_role": "Senior Researcher",
    "employee_clearance_level": "High"
}

response = requests.put(employee_endpoint, json=updated_info)

if response.status_code == 200:
    print("Employee information updated successfully!")
else:
    print("Failed to update employee information. Status code:", response.status_code)

```

#### Deleting a genome entry
```{python}
import requests

base_url = "https://seq-lan-api-0f260ca5bb66.herokuapp.com/"
genome_id = 8  # Replace with an existing genome entry ID
genome_endpoint = f"{base_url}genome/{genome_id}"

response = requests.delete(genome_endpoint)

if response.status_code == 200:
    print("Genome entry deleted successfully!")
else:
    print("Failed to delete genome entry. Status code:", response.status_code)

```

### Using a Web Browser

Alternatively, you can interact with the API endpoints through your web browser:

- **Base URL**: `https://seq-lan-api-0f260ca5bb66.herokuapp.com/` or `http://localhost:5000` or another specified port.
- **Endpoints**: Append the desired endpoint to the base URL (e.g., `https://seq-lan-api-0f260ca5bb66.herokuapp.com/employees`)
- **Methods**: Use appropriate HTTP methods (`GET`, `POST`, `PUT`, `DELETE`) based on the action you wish to perform.

### Using HTTP Services (e.g., Postman)

For a more comprehensive and controlled interaction with the API, using HTTP services like Postman is recommended:

- **Postman**: Utilize Postman's intuitive interface to send requests to API endpoints, set headers, and manage different HTTP methods conveniently.
- **Base URL**: Same as mentioned above (`https://seq-lan-api-0f260ca5bb66.herokuapp.com/`)

## Link to source code

API source code: <https://github.com/Sahil-Sewani/seq-lab-API/blob/main/seqlabAPI2.py>



