#  Contact class stores a single person's name,phone and email
class Contact():
    def __init__(self,name,phone,email):
        # attributes for one contact
        self.name = name
        self.phone = phone
        self.email = email
    
    def __str__(self):
        return (f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}")

# Contactbook class manages the list of all contacts + file handling
class Contactbook():
    def __init__(self):
        self.list1 = []
        try:
            with open("task.txt","r") as f:
                for line in f:
                    if not line.strip():
                        continue
                    parts = line.strip().split(",")
                    if len(parts) != 3:
                        continue
                    name,phone,email = parts
                    self.list1.append(Contact(name,phone,email))
        except FileNotFoundError:
            pass

    def add_contact(self):
        name = input("Enter name:")
        phone = int(input("Enter phone no:"))
        email = input("Enter email id:")
        new_contact = Contact(name,phone,email)
        self.list1.append(new_contact)
        
        with open("task.txt","a") as f:
            (f.write(f"{name},{phone},{email}\n"))
          
    def view_contacts(self):
        for contact in self.list1:
            print(contact)

    def search_contact(self):
        Enter_name = input("Enter the name you want to search:").lower()
        found = False
        for contact in self.list1:
            if Enter_name == contact.name.lower():
                print(contact)
                found = True
                break
        if not found:
            print("Not found")
                
    def update_contact(self):
        user = input("Enter the contact you want to update:").lower()
        for contact in self.list1:
            if user == contact.name.lower() or user == str(contact.phone):
                print("What do you want to update?")
                print("1.Name")
                print("2.phone")
                print("3.email")
                print("4.All")
                choice = input("Enter your choice:")
                if choice == "1":
                    new_name = input("Enter new name :")
                    contact.name = new_name
                elif choice == "2":
                    new_phone = int(input("Enter new phone:"))
                    contact.phone = new_phone
                elif choice == "3":
                    new_email = input("Enter new email:")
                    contact.email = new_email
                elif choice == "4":
                    new_name = input("Enter new name :")
                    contact.name = new_name

                    new_phone = int(input("Enter new phone:"))
                    contact.phone = new_phone

                    new_email = input("Enter new email:")
                    contact.email = new_email
                    
            print(contact)

    def delete_contact(self):
        remove = input("Enter the contact you want to remove:")
        for contact in self.list1:
            if remove == contact.name or remove == str(contact.phone):
                self.list1.remove(contact)

    def exit_program(self):
        print("Exiting program!")

object = Contactbook()

while True:
    menu = {
        "1": object.add_contact,
        "2": object.view_contacts,
        "3": object.search_contact,
        "4": object.update_contact,
        "5": object.delete_contact,
        }
    print(" 1.Add contact", " 2.View contact"," 3.Search contact"," 4.Update contact"," 5.Delete contact,")
    choice = input("Choose option:")
    if choice in menu:
        menu[choice]()
    elif choice == "6":
        break
    else:
        print("Invalid option!")




    

