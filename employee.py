class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_employee_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ${self.salary}")

def main():
    # Creating instances for different employees
    Ahsan = Employee(name="Ahsan", employee_id="W123", salary=50000)
    Darwesh = Employee(name="Darwesh", employee_id="T456", salary=60000)
    Hamza = Employee(name="Hamza", employee_id="F769", salary=55000)

    # Displaying employee details
    print("Employee Details for Ahsan:")
    Ahsan.display_employee_details()

    print("\nEmployee Details for Darwesh:")
    Darwesh.display_employee_details()

    print("\nEmployee Details for Hamza:")
    Hamza.display_employee_details()

if __name__ == "__main__":
    main()
