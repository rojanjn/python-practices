import csv

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    # def __str__(self):
    #     return f"{self.name} "
    
class List:
    def __init__(self, filename="contacts.csv"):
        self.filename = filename
        self.contacts = []
        self.load_from_csv()
        
    # user adds new contacts to the list
    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_to_csv()
        
    # user removes certain contact from the list
    def remove_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                self.save_to_csv()
                return True
        return False
    
    # user views the contact list
    def show_contacts(self):
        if not self.contacts:
            print("No contacts added to the list.")
        else:
            for i, contact in enumerate(self.contacts, start = 1):
                print(f"{i}.{contact}")
                
    # saving to the csv file
    def save_to_csv(self):
        try:
            with open(self.filename, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Phone", "Email", "Address"])
                
                for contact in self.contacts:
                    writer.writerow([contact.name, contact.phone, contact.email, contact.address])
                    
        except Exception as error:
            print("Error in saving:", error)
            
    # loading the csv file
    def load_from_csv(self):
        try:
            with open(self.filename, "r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                
                for row in reader:
                    contact = Contact(row["Name"], row["Phone"], row["Email"], row["Address"])
                    self.contacts.append(contact)
                    
        except FileNotFoundError:
            pass
        except Exception as error:
            print("Error in loading:", error)
            
# main menu of the application
def menu():
    contactBook = List()
    
    while True:
        try:
            print("\n=-=-=-=-=-=-=-=-=- Contact book Menu =-=-=-=-=-=-=-=-=-")
            print("1. Add Contact")
            print("2. Remove Contact")
            print("3. Show Contacts")
            print("4. Exit")

            choice = input("Enter 1, 2, 3, or 4: ")

            # adding contact
            if choice == "1":
                name = input("Contact's Name: ")
                phone = input("Contact's Phone Number (format: xxx-xxx-xxxx): ")
                email = input("Contact's Email Address: ")
                address = input("Contact's Home Address: ")
                
                contact = Contact(name, phone, email, address)
                
                contactBook.add_contact(contact)
                
                print("Contact Added ✅")
                
            # removing contact
            elif choice == "2":
                name = input("Name of the Contact you'd wish to remove: ")
                if contactBook.remove_contact(name):
                    print("Contact Removed ✅")
                else:
                    print("Contact Not Found ❌")
                    
            # showing contact book
            elif choice == "3":
                contactBook.show_contacts()
                
            # exiting
            elif choice == "4":
                print("Exiting...")
                break
            
            else:
                print("Invalid Input. Try again...")

        except Exception as error:
            print("An Error has Occured", error)
            
    print("\nProgram was successfully implemented.")

if __name__ == "__main__":
    menu()
