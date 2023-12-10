# seq-lab-API

#### Base URL: http://127.0.0.1:5000/

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

<!-- Add similar documentation for Genome and Room routes -->

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



