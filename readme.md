# Contact Management System

The Contact Management System is a Python program designed to efficiently manage contact information. It provides a user-friendly interface for adding, editing, deleting, searching for, and displaying contacts. Additionally, the system allows users to categorize contacts into predefined categories and define custom fields for storing additional information. The contacts are automatically backed up after each addition er editing.

## Functionality Overview

### Add Contact

The `add_contact` function allows users to add a new contact to the system. It prompts the user to input details such as name, email, phone number, additional information, category, and custom fields. Once the contact is successfully added, a backup of the updated contact data is automatically created.

### Edit Contact

The `edit_contact` function enables users to edit existing contact details. It prompts the user to enter the email address of the contact to be edited and allows them to modify the contact's name, phone number, additional information, category, and custom fields. After the changes are saved, a backup of the updated contact data is automatically created.

### Delete Contact

The `delete_contact` function allows users to remove a contact from the system. It prompts the user to enter the email address of the contact to be deleted and removes the contact from the contact list. A backup of the updated contact data is automatically created after the contact is deleted.

### Search Contact

The `search_contact` function enables users to search for a contact by name, phone number, email address, or additional information. It prompts the user to enter the search query and displays the contact details if a matching contact is found.

### Display All Contacts

The `display_all_contacts` function displays a list of all contacts along with their details. It prompts the user to specify a sorting option (by name, category, email, or none) and arranges the contacts accordingly. Custom fields for each contact are also displayed if they exist.

### Export contacts as txt

The `export_contacts` function export all recorded contacts as tct file.

### Import txt contacts

The `import_contacts` function imports contacts from a txt file.

## Others

### Categorize Contacts

The `categories` attribute allows users to categorize contacts into predefined categories such as Friends, Family, and Colleagues. When adding or editing a contact, the user can choose the appropriate category from the predefined list.

### Define Custom Fields

Users can define custom fields for contacts to store additional information beyond the standard fields. When adding or editing a contact, the user is prompted to specify the key name and value for each custom field. These custom fields can be anything the user desires, such as birthdays, anniversaries, addresses, or any other relevant information.

## Adding Categories and Custom Fields

To add new categories or define custom fields:

1. **Categories:** Open the `categories` attribute in the `ContactManagementSystem` class and add new category names as strings to the list. These categories will be available for selection when adding or editing contacts.

2. **Custom Fields:** When adding or editing a contact, the system prompts the user to define custom fields. Enter the desired key name and value for each custom field when prompted. These custom fields will be stored along with the standard contact information and displayed when viewing the contact details.

The Contact Management System is designed to streamline contact management tasks and ensure that your contact information is always accessible and up to date.

## Getting Started

To run the Contact Management System:

1. Clone the repository to your local machine.
2. Ensure you have Python installed on your system.
3. Open a terminal or command prompt and navigate to the directory containing the `mini-project.py` file.
4. Run the following command to execute the program:

   ```bash
   python mini-project.py
   ```

## Requirements

- Python 3.x
