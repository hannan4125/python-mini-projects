# Contact Book Program using Python
# Features: Add, View, Search, Delete, Clear, Update contacts
# Contacts are saved in a JSON file for persistence
# Supports sorting by name or phone

import json
# JSON file to store contacts

FILE = "contacts.json"
# Load contacts from the JSON file, return empty list if file doesn't exist
def load_contacts():
    try:
        with open(FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Save contacts to the JSON file with indentation    
def save_contacts(contacts):
    with open(FILE, 'w') as f:
        json.dump(contacts, f, indent=5)


# Get contact information from user input
# Validate name, phone number, and email format
# Check if contact already exists
# Append new contact to the contacts list
def add_contact(contacts):
    name = input("Enter your name: ").strip().title()
    phone = input("Enter contact number: ")
    email = input("Enter email address: ").strip()

    if not name or not phone or not email:
        print("❌ All info is required!")
        return
    
    if not all(part.isalpha() for part in name.split()):
        print("❌ Name must only contain alphabets and spaces!")
        return
    
    if not phone.isdigit():
        print("❌ Phone number must be in digits!")
        return 
    
    if len(phone) < 7 or len(phone) > 15:
        print("❌ Phone number length must be between 7 and 15 digits!")
        return
    
    if "@" not in email or "." not in email.split("@")[-1]:
        print("❌ Invalid email format!")
        return
    
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("❌ Contact already exists!")
            return
    
    contacts.append({"name": name, "phone": phone, "email": email})
    print(f"\n✔ Contact '{name}' added successfully.")
    
# Return message if contacts list is empty
# Sort contacts by name or phone if requested
# Print formatted contact list with index
def view_contact(contacts, sort_by=None):
    if not contacts:
        print("📲 No contacts available!")
        return
    
    if sort_by == "name":
        contacts = sorted(contacts, key=lambda x: x['name'].lower())
    elif sort_by == "phone":
        contacts = sorted(contacts, key=lambda x: x['phone'])
    
    print("\n----- Contact List ------")
    print("Name".ljust(23), "Phone".ljust(23), "Email")
    print("-" * 60)
    
    for i, contact in enumerate(contacts,start=1):
        print(f"{i}. {contact['name'].ljust(20)} {contact['phone'].ljust(20)} {contact['email']}")
            
# Return message if contacts list is empty
# Collect contacts that match the search query
# Print search results in formatted style        
def search_contact(contacts):
    if not contacts:
        print("❌ No contacts available to search!")
        return
    
    query = input("🔍 Enter name, phone, or email to search: ").strip().lower()
    found = []
    
    for contact in contacts:
        if (query in contact["name"].lower() or
            query in contact["phone"] or
            query in contact["email"].lower()):
            found.append(contact)
    if not found:
        print("❌ No matching contact found!")
        return
    
    print("\n" f"----- 🔍 Search Results for '{query}' -----")
    print("Name".ljust(23), "Phone".ljust(23), "Email")
    print("-" * 60)
    
    for i, contact in enumerate(found,start=1):
        print(f"{i}. {contact['name'].ljust(20)} {contact['phone'].ljust(20)} {contact['email']}")   

# Return message if contacts list is empty
# Ask user which contact to delete
# Validate input and remove the selected contact
def delete_contact(contacts):
    if not contacts:
        print("❌ No contacts available to delete!")
        return
    view_contact(contacts)
    try:
        delete = int(input("Enter contact number to delete: "))
        if 1 <= delete <= len(contacts):
            removed = contacts.pop(delete - 1)
            print(f"✔ Contact '{removed['name']}' deleted successfully.")
        else:
            print("❌ Invalid contact number!")
    except ValueError:
        print("❌ Please enter a valid number!")

# Return message if contacts list is empty
# Ask for confirmation before clearing all contacts
# Clear all contacts if confirmed
def clear_contact(contacts):
    if not contacts:
        print("❌ No contacts available!")
        return
    confirm = input("Do you want to clear all contacts? (yes/no): ").strip().lower()
    if confirm == "yes":
        contacts.clear()
        print(f"✔ All contacts are cleared.")
    elif confirm == "no":
        print("😊 Thanks for the confirmation.")
    else:
        print("❌ Invalid information! Please type 'yes' or 'no'.")

# Return message if contacts list is empty
# Ask user which contact to update
# Validate user input for number
# Ask which field to update (name/phone/email/all)
# Validate new data before updating
# Update the contact with new information
def update_contact(contacts):
    if not contacts:
        print("❌ No contacts available to update!")
        return
    view_contact(contacts)
    
    try:
        update = int(input("Enter contact number to update: "))
    except ValueError:
        print("❌ Please enter a valid number!")
        return
    
    if 1 <= update <= len(contacts):
        confirm = input("What do you want to update? (name/phone/email/all): ").strip().lower()
        if confirm == "name":
            new_name = input("Enter new name: ").strip().title()
            if not new_name or not all(part.isalpha() for part in new_name.split()):
                print("❌ Name must only contain alphabets and spaces!")
            else:
                contacts[update - 1]['name'] = new_name
                print(f"✔ Contact name updated.")
        
        elif confirm == "phone":
            new_phone = input("Enter new phone number: ").strip()
            if not new_phone.isdigit() or len(new_phone) < 7 or len(new_phone) > 15:
                print("❌ Phone number must be in digits and between 7 and 15 digits!")
            else:
                contacts[update - 1]['phone'] = new_phone
                print("✔ Phone number updated.")
        
        elif confirm == "email":
            new_email = input("Enter new email: ").strip()
            if "@" not in new_email or "." not in new_email.split("@")[-1]:
                print("❌ Invalid email format!")
            else:
                contacts[update - 1]['email'] = new_email
                print("✔ Contact email updated.")
        
        elif confirm == "all":
            new_name = input("Enter new name: ").strip().title()
            new_phone = input("Enter new phone number: ").strip()
            new_email = input("Enter new email: ").strip()
            
            if not new_name or not all(part.isalpha() for part in new_name.split()):
                print("❌ Name must contain only alphabets and spaces!")
            elif not new_phone.isdigit() or not (7 <= len(new_phone) <= 15):
                print("❌ Phone number must be in digits and between 7 and 15 digits!")
            elif "@" not in new_email or "." not in new_email.split("@")[-1]:
                print("❌ Invalid email format!")
            else:
                contacts[update - 1]['name'] = new_name
                contacts[update - 1]['phone'] = new_phone
                contacts[update - 1]['email'] = new_email
                print("✔ All contact details updated successfully!")
    else:
        print("❌ Invalid contact number!") 

# Load contacts from file at the start
# Show main menu and loop until user exits
# Call corresponding functions based on user choice
# Save contacts to file after changes
# Handle invalid menu choice
def main():
    contacts = load_contacts()
    while True:
        print("\n---- Contact Book Menu ----")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Clear all Contacts")
        print("6. Update Contact")
        print("7. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_contact(contacts)
            save_contacts(contacts)
        elif choice == "2":
            sort_choice = input("Sort by (name/phone/none): ").strip().lower()
            if sort_choice not in ['name', 'phone', 'none']:
                print("❌ Invalid choice! Showing unsorted contacts.")
                sort_choice = None
            elif sort_choice == "None":
                sort_choice = None
            view_contact(contacts,sort_by=sort_choice)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
            save_contacts(contacts)
        elif choice == "5":
            clear_contact(contacts)
            save_contacts(contacts)
        elif choice == "6":
            update_contact(contacts)
            save_contacts(contacts)
        elif choice == "7":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please choose between (1-7).")

# Run the program if executed directly
if __name__ == "__main__":
    main()
