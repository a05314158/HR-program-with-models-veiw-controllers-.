def show_menu():
    print("1. View employee list\n2. Add employee\n3. Edit employee\n4. Delete employee\n5. Exit")

def show_employees(data):
    for entry in data:
        print(f"{entry[0]} {entry[1]}, {entry[2]}, Salary: {entry[3]}")

def get_user_input(message):
    return input(message)

def display_message(message):
    print(message)
