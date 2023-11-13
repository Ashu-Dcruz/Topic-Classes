class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def main():
    # Creating an instance of the Person class
    ahsan = Person(name="Ahsan", age=19)

    # Printing out the person's details
    print(f"Person's Name: {ahsan.name}")
    print(f"Person's Age: {ahsan.age}")

if __name__ == "__main__":
    main()
