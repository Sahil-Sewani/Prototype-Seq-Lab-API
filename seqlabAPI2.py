from flask import Flask, request, jsonify, render_template
import pymysql

app = Flask(__name__)

# Database Configuration
connection = pymysql.connect(
    host='cmsc508.com',
    database='23FA_groups_group16',
    user='23FA_sewanis',
    password='Shout4_sewanis_GOME'
)

# Homepage Route
@app.route('/')
def homepage():
    return render_template('homepage.html')

# EMPLOYEE TABLE

# GET Method Routes
@app.route('/employees', methods=['GET'])
def get_employees():
    with connection.cursor() as cursor:
        sql = "SELECT * FROM employee"
        cursor.execute(sql)
        result = cursor.fetchall()
    return jsonify(result)

# GET Method Route to get details of a specific employee by ID
@app.route('/employees/<int:employee_id>', methods=['GET'])
def get_employee_by_id(employee_id):
    if request.method == 'GET':
        with connection.cursor() as cursor:
            sql = "SELECT * FROM employee WHERE employee_id = %s"
            cursor.execute(sql, (employee_id,))
            result = cursor.fetchone()
        if result:
            return jsonify(result)
        else:
            return 'Employee not found', 404
    else:
        return 'Method not allowed', 405

# POST Method Route for adding a new employee
@app.route('/employees', methods=['POST'])
def add_employee():
    data = request.get_json()
    employee_id = data['employee_id']
    employee_name = data['employee_name']
    employee_role = data['employee_role']
    employee_clearance_level = data['employee_clearance_level']
    with connection.cursor() as cursor:
        sql = "INSERT INTO employee (employee_id, employee_name, employee_role, employee_clearance_level) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (employee_id, employee_name, employee_role, employee_clearance_level))
        connection.commit()
    return 'Employee added successfully', 201

# PUT Method Route for updating an employee
@app.route('/employees/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    data = request.get_json()
    employee_name = data['employee_name']
    employee_role = data['employee_role']
    employee_clearance_level = data['employee_clearance_level']
    with connection.cursor() as cursor:
        sql = "UPDATE employee SET employee_name=%s, employee_role=%s, employee_clearance_level=%s WHERE employee_id=%s"
        cursor.execute(sql, (employee_name, employee_role, employee_clearance_level, employee_id))
        connection.commit()
    return 'Employee updated successfully'

# DELETE Method Route for deleting an employee
@app.route('/employees/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    with connection.cursor() as cursor:
        sql = "DELETE FROM employee WHERE employee_id=%s"
        cursor.execute(sql, (employee_id,))
        connection.commit()
    return 'Employee deleted successfully'

# CONSUMABLE TABLE

# POST Method Route for adding a new consumable
@app.route('/consumables', methods=['POST'])
def add_consumable():
    data = request.get_json()
    consumable_name = data['consumable_name']
    quantity = data['quantity']
    room_id = data['room_id']
    with connection.cursor() as cursor:
        sql = "INSERT INTO consumable (consumable_name, quantity, room_id) VALUES (%s, %s, %s)"
        cursor.execute(sql, (consumable_name, quantity, room_id))
        connection.commit()
    return 'Consumable added successfully', 201

# GET Method Route for retrieving all consumables
@app.route('/consumables', methods=['GET'])
def get_consumables():
    with connection.cursor() as cursor:
        sql = "SELECT * FROM consumable"
        cursor.execute(sql)
        result = cursor.fetchall()
    return jsonify(result)

# GET Method Route for retrieving a specific consumable by consumable_id
@app.route('/consumables/<int:consumable_id>', methods=['GET'])
def get_consumable(consumable_id):
    with connection.cursor() as cursor:
        sql = "SELECT * FROM consumable WHERE consumable_id = %s"
        cursor.execute(sql, (consumable_id,))
        result = cursor.fetchone()
    if result:
        return jsonify(result)
    else:
        return 'Consumable not found', 404

# PUT Method Route for updating a specific consumable by consumable_id
@app.route('/consumables/<int:consumable_id>', methods=['PUT'])
def update_consumable(consumable_id):
    data = request.get_json()
    consumable_name = data['consumable_name']
    quantity = data['quantity']
    room_id = data['room_id']
    with connection.cursor() as cursor:
        sql = "UPDATE consumable SET consumable_name=%s, quantity=%s, room_id=%s WHERE consumable_id=%s"
        cursor.execute(sql, (consumable_name, quantity, room_id, consumable_id))
        connection.commit()
    return 'Consumable updated successfully'

# DELETE Method Route for deleting a specific consumable by consumable_id
@app.route('/consumables/<int:consumable_id>', methods=['DELETE'])
def delete_consumable(consumable_id):
    with connection.cursor() as cursor:
        sql = "DELETE FROM consumable WHERE consumable_id=%s"
        cursor.execute(sql, (consumable_id,))
        connection.commit()
    return 'Consumable deleted successfully'

# EQUIPMENT TABLE

# POST Method Route for adding a new equipment
@app.route('/equipment', methods=['POST'])
def add_equipment():
    data = request.get_json()
    name = data['name']
    model = data['model']
    room_id = data['room_id']
    with connection.cursor() as cursor:
        sql = "INSERT INTO equipment (name, model, room_id) VALUES (%s, %s, %s)"
        cursor.execute(sql, (name, model, room_id))
        connection.commit()
    return 'Equipment added successfully', 201

# GET Method Route for retrieving all equipment
@app.route('/equipment', methods=['GET'])
def get_equipment():
    with connection.cursor() as cursor:
        sql = "SELECT * FROM equipment"
        cursor.execute(sql)
        result = cursor.fetchall()
    return jsonify(result)

# GET Method Route for retrieving a specific equipment by equipment_id
@app.route('/equipment/<int:equipment_id>', methods=['GET'])
def get_specific_equipment(equipment_id):
    with connection.cursor() as cursor:
        sql = "SELECT * FROM equipment WHERE equipment_id = %s"
        cursor.execute(sql, (equipment_id,))
        result = cursor.fetchone()
    if result:
        return jsonify(result)
    else:
        return 'Equipment not found', 404

# PUT Method Route for updating a specific equipment by equipment_id
@app.route('/equipment/<int:equipment_id>', methods=['PUT'])
def update_equipment(equipment_id):
    data = request.get_json()
    name = data['name']
    model = data['model']
    room_id = data['room_id']
    with connection.cursor() as cursor:
        sql = "UPDATE equipment SET name=%s, model=%s, room_id=%s WHERE equipment_id=%s"
        cursor.execute(sql, (name, model, room_id, equipment_id))
        connection.commit()
    return 'Equipment updated successfully'


# DELETE Method Route for deleting a specific equipment by equipment_id
@app.route('/equipment/<int:equipment_id>', methods=['DELETE'])
def delete_equipment(equipment_id):
    with connection.cursor() as cursor:
        sql = "DELETE FROM equipment WHERE equipment_id=%s"
        cursor.execute(sql, (equipment_id,))
        connection.commit()
    return 'Equipment deleted successfully'


# GENOME TABLE

# POST Method Route for adding a new genome entry
@app.route('/genome', methods=['POST'])
def add_genome():
    data = request.get_json()
    equipment_id = data['equipment_id']
    sequence_type = data['type']
    species_name = data['species_name']
    sequence = data['the_sequence']
    with connection.cursor() as cursor:
        sql = "INSERT INTO genome (equipment_id, type, species_name, the_sequence) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (equipment_id, sequence_type, species_name, sequence))
        connection.commit()
    return 'Genome entry added successfully', 201

# GET Method Route for retrieving all genome entries
@app.route('/genome', methods=['GET'])
def get_genome():
    with connection.cursor() as cursor:
        sql = "SELECT * FROM genome"
        cursor.execute(sql)
        result = cursor.fetchall()
    return jsonify(result)

# GET Method Route for retrieving a specific genome entry by genome_id
@app.route('/genome/<int:genome_id>', methods=['GET'])
def get_specific_genome(genome_id):
    with connection.cursor() as cursor:
        sql = "SELECT * FROM genome WHERE genome_id = %s"
        cursor.execute(sql, (genome_id,))
        result = cursor.fetchone()
    if result:
        return jsonify(result)
    else:
        return 'Genome entry not found', 404

# PUT Method Route for updating a specific genome entry by genome_id
@app.route('/genome/<int:genome_id>', methods=['PUT'])
def update_genome(genome_id):
    data = request.get_json()
    equipment_id = data['equipment_id']
    sequence_type = data['type']
    species_name = data['species_name']
    sequence = data['the_sequence']
    with connection.cursor() as cursor:
        sql = "UPDATE genome SET equipment_id=%s, type=%s, species_name=%s, the_sequence=%s WHERE genome_id=%s"
        cursor.execute(sql, (equipment_id, sequence_type, species_name, sequence, genome_id))
        connection.commit()
    return 'Genome entry updated successfully'

# DELETE Method Route for deleting a specific genome entry by genome_id
@app.route('/genome/<int:genome_id>', methods=['DELETE'])
def delete_genome(genome_id):
    with connection.cursor() as cursor:
        sql = "DELETE FROM genome WHERE genome_id=%s"
        cursor.execute(sql, (genome_id,))
        connection.commit()
    return 'Genome entry deleted successfully'

# ROOM TABLE

# GET Method Route for retrieving all rooms
@app.route('/rooms', methods=['GET'])
def get_rooms():
    with connection.cursor() as cursor:
        sql = "SELECT * FROM room"
        cursor.execute(sql)
        result = cursor.fetchall()
    return jsonify(result)

# GET Method Route for retrieving a specific room by room number
@app.route('/rooms/<int:room_number>', methods=['GET'])
def get_room_by_number(room_number):
    with connection.cursor() as cursor:
        sql = "SELECT * FROM room WHERE room_number = %s"
        cursor.execute(sql, (room_number,))
        result = cursor.fetchone()
    if result:
        return jsonify(result)
    else:
        return 'Room not found', 404

# POST Method Route for adding a new room
@app.route('/rooms', methods=['POST'])
def add_room():
    data = request.get_json()
    room_number = data['room_number']
    room_description = data.get('room_description', None)  # optional field
    room_type = data.get('room_type', None)  # new field
    with connection.cursor() as cursor:
        sql = "INSERT INTO room (room_number, room_description, room_type) VALUES (%s, %s, %s)"
        cursor.execute(sql, (room_number, room_description, room_type))
        connection.commit()
    return 'Room added successfully', 201

# PUT Method Route for updating a room by room number
@app.route('/rooms/<int:room_number>', methods=['PUT'])
def update_room(room_number):
    data = request.get_json()
    room_description = data.get('room_description', None)  # optional field
    room_type = data.get('room_type', None)  # new field
    with connection.cursor() as cursor:
        sql = "UPDATE room SET room_description=%s, room_type=%s WHERE room_number=%s"
        cursor.execute(sql, (room_description, room_type, room_number))
        connection.commit()
    return 'Room updated successfully'

# DELETE Method Route for deleting a room by room number
@app.route('/rooms/<int:room_number>', methods=['DELETE'])
def delete_room(room_number):
    with connection.cursor() as cursor:
        sql = "DELETE FROM room WHERE room_number=%s"
        cursor.execute(sql, (room_number,))
        connection.commit()
    return 'Room deleted successfully'



if __name__ == '__main__':
    app.run()