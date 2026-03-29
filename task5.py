# Contact Book Program

contacts = []

# Function to add contact
def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print("✅ Contact added successfully!")

# Function to view contacts
def view_contacts():
    print("\n--- Contact List ---")
    if not contacts:
        print("No contacts found.")
        return

    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")

# Function to search contact
def search_contact():
    print("\n--- Search Contact ---")
    search = input("Enter name or phone: ").lower()

    found = False
    for contact in contacts:
        if search in contact["name"].lower() or search in contact["phone"]:
            print("\nContact Found:")
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            print("Address:", contact["address"])
            found = True

    if not found:
        print("❌ Contact not found.")

# Function to update contact
def update_contact():
    print("\n--- Update Contact ---")
    name = input("Enter name of contact to update: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            print("Enter new details:")
            contact["phone"] = input("New phone: ")
            contact["email"] = input("New email: ")
            contact["address"] = input("New address: ")
            print("✅ Contact updated successfully!")
            return

    print("❌ Contact not found.")

# Function to delete contact
def delete_contact():
    print("\n--- Delete Contact ---")
    name = input("Enter name of contact to delete: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            contacts.remove(contact)
            print("✅ Contact deleted successfully!")
            return

    print("❌ Contact not found.")

# Main menu loop
while True:
    print("\n====== CONTACT BOOK MENU ======")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Exiting Contact Book. Goodbye! 👋")
        break
    else:
        print("❌ Invalid choice. Please try again.")