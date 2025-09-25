import os
FILEName="Contact.txt"
if not os .path.exists(FILEName):
    with open (FILEName,"w") as f:
        pass

def add_contact():
    name=input("Enter name: ")
    phone=input("Enter phone: ")
    email=input("Enter email: ")

    with open (FILEName,"a") as f:
        f.write(f"{name}|{phone}|{email}\n")
        print("contact added!\n")
            
def view_contact():
    with open(FILEName,"r") as f:
        lines=f.readlines()
        if not lines:
            print("No contact found.\n")
            return
        print("\n All contacts:")
        for line in lines:
            name, phone, email = line.strip().split("|")
            print(f"Name:{name},phone:{phone},Eamil:{email}")
            print()

def search_contact():
        search_name= input("Enter name to search:").lower()
        found=False
        with open (FILEName,"r") as f:
            for line in f:
                name,phone,email= line.strip().split("|")
                if name.lower()==search_name:
                    print(f"Found Name:{name},phone:{phone},Email:{email}\n")
                    fond=True
                    break
                if not found:
                     print("Contact not found")
    
def Remove_contact():
        remove_name=input("Enter name to remove:").lower()
        new_contact=[]
        found=False
        with open (FILEName,"r") as f:
            for line  in f:
                name,phone,email=line.strip().split("|")
                if name.lower()!=remove_name:
                    new_contact.append(line)
                else:
                    found=True
            if found:
                with open (FILEName,"w") as f:
                    f.writelines(new_contact)
                    print("Contact removed!\n")

while True:
    print("===Contact manger===")
    print("1.Addcontact")
    print("2.View all contact")
    print("3.Search contact")
    print("4.Remove contact")
    print("5.exist")

    choice=input("Enter youe choice: ")
    if choice=="1":
        add_contact()
    elif choice=="2":
        view_contact()
    elif choice=="3":
        search_contact()
    elif choice =="4":
        Remove_contact()
    elif choice =="5":
        print("Existing...Good Bye!")
        break
    else:
        print("invalid choice Try again.\n")

                