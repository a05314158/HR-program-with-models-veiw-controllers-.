EMPLOYEES_FILE = 'employees.txt'

def read_data():
    try:
        with open(EMPLOYEES_FILE, 'r') as file:
            return [line.strip().split(',') for line in file]
    except FileNotFoundError:
        return []

def write_data(data):
    with open(EMPLOYEES_FILE, 'w') as file:
        for entry in data:
            file.write(','.join(entry) + '\n')
