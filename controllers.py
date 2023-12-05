from models import read_data, write_data
from views import show_menu, show_employees, get_user_input, display_message


def add_employee():
    new_employee = [get_user_input(f"Enter {field}: ") for field in ['name', 'surname', 'position', 'salary']]
    write_data(new_employee)
    display_message("Employee added!")


def edit_employee(data):
    employee_identifier = get_user_input("Enter name and surname of the employee to edit (comma-separated): ")
    name_to_edit, surname_to_edit = map(str.strip, employee_identifier.split(','))

    for entry in data:
        if (entry[0].strip(), entry[1].strip()) == (name_to_edit, surname_to_edit):
            new_values = [get_user_input(f"Enter new {field} ({entry[i]}): ") or entry[i] for i, field in
                          enumerate(['name', 'surname', 'position', 'salary'])]
            data.remove(entry)
            data.append(new_values)
            write_data(data)
            display_message("Employee edited!")
            return
    display_message("Employee not found!")


def delete_employee(data):
    employee_identifier = get_user_input("Enter name and surname of the employee to delete (comma-separated): ")
    name_to_delete, surname_to_delete = map(str.strip, employee_identifier.split(','))

    data = [entry for entry in data if (entry[0].strip(), entry[1].strip()) != (name_to_delete, surname_to_delete)]
    write_data(data)
    display_message("Employee deleted!")


def main():
    while True:
        show_menu()

        actions = {
            '1': lambda: show_employees(read_data()),
            '2': add_employee,
            '3': lambda: edit_employee(read_data()),
            '4': lambda: delete_employee(read_data()),
            '5': lambda: exit()
        }

        choice = get_user_input("Choose an action (enter the number): ")
        actions.get(choice, lambda: display_message("Invalid input. Try again."))()


if __name__ == "__main__":
    main()
