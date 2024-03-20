import re
import json

class ContactManagementSystem:
    def __init__(self):
        self.contacts = {}
        self.categories = ["Friends", "Family", "Colleagues"]

    def validate_email(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$'
        return re.match(pattern, email) is not None

    def input_email(self):
        while True:
            email = input("Enter email address: ")
            if self.validate_email(email):
                return email
            print("Invalid email format. Please try again.")

    def validate_phone(self, phone):
        pattern = r'^\+?[0-9]{10,15}$'
        return re.match(pattern, phone) is not None

    def input_phone(self):
        while True:
            phone = input("Enter phone number: ")
            if self.validate_phone(phone):
                return phone
            print("Invalid phone format. Please try again.")

    def add_contact(self):
        print("\n-- Add a New Contact --")
        email = self.input_email()
        if email in self.contacts:
            print("A contact with this email already exists.")
            return
        name = input("Enter name: ")
        phone = self.input_phone()
        additional_info = input("Enter additional info: ")
        category = self.choose_category()
        custom_fields = {}
        add_custom = input("Do you want to add custom fields? (yes/no): ").lower()
        if add_custom == "yes":
            custom_fields = self.input_custom_fields()
        self.contacts[email] = {
            "Name": name,
            "Email": email,
            "Phone": phone,
            "Additional Info": additional_info,
            "Category": category,
            **custom_fields
        }
        print("Contact added successfully.")
        self.export_contacts()
    def input_custom_fields(self):
        custom_fields = {}
        while True:
            field_name = input("Enter custom field name (leave blank to finish): ")
            if not field_name:
                break
            field_value = input(f"Enter value for {field_name}: ")
            custom_fields[field_name] = field_value
        return custom_fields

    def choose_category(self):
        while True:
            print("Choose category:")
            for i, category in enumerate(self.categories, 1):
                print(f"{i}. {category}")
            choice = input("Enter category number: ")
            if choice.isdigit() and 1 <= int(choice) <= len(self.categories):
                return self.categories[int(choice) - 1]
            print("Invalid choice. Please try again.")

    def edit_contact(self):
        print("\n-- Edit Existing Contact --")
        email = self.input_email()
        if email in self.contacts:
            name = input("Enter name: ")
            phone = self.input_phone()
            additional_info = input("Enter additional info: ")
            category = self.choose_category()
            custom_fields = {}
            for key in self.contacts[email]:
                if key not in ["Name", "Email", "Phone", "Additional Info", "Category"]:
                    custom_fields[key] = input(f"Enter value for {key}: ")
            self.contacts[email].update({
                "Name": name,
                "Phone": phone,
                "Additional Info": additional_info,
                "Category": category,
                **custom_fields
            })
            print("Contact edited successfully.")
        else:
            print("Contact not found.")
        self.export_contacts()

    def delete_contact(self):
        email = self.input_email()
        if email in self.contacts:
            del self.contacts[email]
            print(f"Contact with email {email} has been deleted.")
        else:
            print("Contact not found.")

    def search_contact(self):
        search_term = input("Enter search term: ").lower()
        found_contacts = []
        for email, contact in self.contacts.items():
            if (
                search_term in contact['Name'].lower() or
                search_term in contact['Email'].lower() or
                search_term in contact['Phone'].lower() or
                search_term in contact['Additional Info'].lower()
            ):
                found_contacts.append((email, contact))
        if found_contacts:
            print("Found contacts:")
            for email, contact in found_contacts:
                print(f"Email: {email}")
                print(f"Name: {contact['Name']}")
                print(f"Phone: {contact['Phone']}")
                print(f"Additional Info: {contact['Additional Info']}")
                print(f"Category: {contact['Category']}")
                print()
        else:
            print("No contacts found.")


    def display_all_contacts(self):
        if self.contacts:
            sort_option = input("Enter sorting option (1. By Name, 2. By Category, 3. By Email, 4. None): ")
            sorted_contacts = []

            if sort_option == '1':
                sorted_contacts = sorted(self.contacts.items(), key=lambda x: x[1]['Name'])
            elif sort_option == '2':
                sorted_contacts = sorted(self.contacts.items(), key=lambda x: x[1]['Category'])
            elif sort_option == '3':
                sorted_contacts = sorted(self.contacts.items(), key=lambda x: x[0])  # Sort by email
            else:
                print("Displaying unsorted contacts.")
                sorted_contacts = self.contacts.items()

            if sorted_contacts:
                for email, contact in sorted_contacts:
                    print(f"\nContact Details:")
                    print(f"Email: {email}")
                    print(f"Name: {contact['Name']}")
                    print(f"Phone: {contact['Phone']}")
                    print(f"Additional Info: {contact['Additional Info']}")
                    print(f"Category: {contact['Category']}")
                    print("Custom Fields:")
                    for key, value in contact.items():
                        if key not in ["Name", "Email", "Phone", "Additional Info", "Category"]:
                            print(f"{key}: {value}")
            else:
                print("No contacts found.")
        else:
            print("No contacts found.")




    def export_contacts(self, filename='contacts.txt'):
        try:
            with open(filename, 'w') as f:
                json.dump(self.contacts, f, indent=4)
            print(f"All contacts have been exported to {filename}.")
        except Exception as e:
            print(f"An error occurred while exporting contacts: {e}")

    def import_contacts(self, filename='contacts.txt'):
        try:
            with open(filename, 'r') as f:
                self.contacts = json.load(f)
            print(f"All contacts have been imported from {filename}.")
        except Exception as e:
            print(f"An error occurred while importing contacts: {e}")

    def run(self):
        print("Welcome to the Contact Management System!")
        while True:
            print("\nMenu:\n1. Add a new contact\n2. Edit an existing contact\n3. Delete a contact\n4. Search for a contact\n5. Display all contacts\n6. Export contacts to a text file\n7. Import contacts from a text file\n8. Quit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.edit_contact()
            elif choice == '3':
                self.delete_contact()
            elif choice == '4':
                self.search_contact()
            elif choice == '5':
                self.display_all_contacts()
            elif choice == '6':
                self.export_contacts()
            elif choice == '7':
                self.import_contacts()
            elif choice == '8':
                print("Quitting the application.")
                break
            else:
                print("Option not implemented yet.")

if __name__ == '__main__':
    cms = ContactManagementSystem()
    cms.run()
