class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def display_contact_details(self):
        print(f"Name: {self.name}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Email: {self.email}")
        print("-" * 25)

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def display_address_book(self):
        print("Address Book:")
        for contact in self.contacts:
            contact.display_contact_details()

def main():
    # Creating contacts
    contact1 = Contact(name="Ahsan Iqbal", phone_number="123-456-7890", email="Ahsan@example.com")
    contact2 = Contact(name="Darwesh Khan", phone_number="987-654-3210", email="Darwesh@example.com")

    # Creating an address book
    address_book = AddressBook()

    # Adding contacts to the address book
    address_book.add_contact(contact1)
    address_book.add_contact(contact2)

    # Displaying address book
    address_book.display_address_book()

if __name__ == "__main__":
    main()
