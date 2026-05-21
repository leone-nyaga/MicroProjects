#!/usr/bin/python3

import json


class ContactBook:
    """
    A simple contact book application that allows users to add,
    view, search, update, and delete contacts
    """

    def __init__(self):
        """
        Initialize an empty list.

        """
        self.contacts = []
        self.load_contacts()

    def main_menu(self):
        """
        Display main menu to the users.
        """
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

    def add_contact(self):
        """
        Add new contact to list
        """
        print("\nAdding a new contact...")
        name = input("Enter Name: ").strip()
        phone_number = input("Enter Phone Number: ").strip()

        contact = {
                "name": name,
                "phone_number": phone_number
        }

        self.contacts.append(contact)
        self.save_contacts()
        print("Contact added successfully!")

    def view_contacts(self):
        """
        Display all saved contacts.

        If no contacts exist, notify the user.
        """
        if not self.contacts:
            print("No contacts available.")
            return

        print("\n--- All Contacts ---\n")

        for contact in self.contacts:
            print(f"Name: {contact['name']}")
            print(f"Phone number: {contact['phone_number']}")
            print()

    def search_contact(self):
        """
        Search for a contact by name.
        """
        search_name = input("Enter name: ").lower()

        print("Searching Contacts...")

        found = False

        for contact in self.contacts:
            if search_name in contact['name'].lower():
                print(f"Name: {contact['name']}")
                print(f"Phone Number: {contact['phone_number']}")
                found = True

        if not found:
            print("No contact found.")

    def update_contact(self):
        """
        Update the phone number of an existing contact.
        """
        update_name = input("Enter contact name to update: ").lower()

        found = False

        for contact in self.contacts:
            if contact['name'].lower() == update_name:

                new_phone = input("Enter new phone number: ").strip()

                contact['phone_number'] = new_phone

                self.save_contacts()

                print("Contact updated successfully!")

                found = True
                break

        if not found:
            print("Contact not found.")


    def delete_contact(self):
        """
        Delete a contact from the contact list.
        """
        delete_name = input("Enter name: ").lower()

        print("Deleting Contact...")

        found = False

        for contact in self.contacts:
            if contact['name'].lower() == delete_name:
                self.contacts.remove(contact)
                self.save_contacts()
                found = True
                print("Contact deleted successfully!")
                break

        if not found:
            print("Contact not found.")

    def load_contacts(self):
        """
        Load contacts from the JSON file into the contacts list.

        Raises:
            json.JSONDecodeError: If the JSON file contains invalid data.
        """
        try:
            with open("contacts.json", "r") as file:
                self.contacts = json.load(file)

        except FileNotFoundError:
            self.contacts = []

    def save_contacts(self):
        """
        Saves contacts to the JSON file.
        """
        with open("contacts.json", "w") as file:
            json.dump(self.contacts, file, indent=4)

    def run(self):
        """
        Run the contact book application.
        """
        while True:
            self.main_menu()

            choice = input("Pick an option: ")

            if choice == "1":
                self.add_contact()

            elif choice == "2":
                self.view_contacts()

            elif choice == "3":
                self.search_contact()

            elif choice == "4":
                self.update_contact()

            elif choice == "5":
                self.delete_contact()

            elif choice == "6":
                print("Bye")
                break
            else:
                print("Invalid!")
