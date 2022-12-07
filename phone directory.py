print(" 1.Add new contact \n 2.Search contact \n 3.Display Contact 4.Edit contact \n 5.Delete Contact \n 6.Exit")

def display_contact():
    print("NAME\t\tCONTACT NUMBER")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))
contact={}
while True:
# choices for contact
    choice=int(input("choice: "))
    if choice==1:
        name=input("Enter contact name: ")
        phone=input("Enter mobile no: ")
        contact[name]=phone
    elif choice==2:
        search_name=input("Enter contact name: ")
        if search_name in contact:
            print(search_name,"'s contact number is ",contact[search_name])
        else:print("Name is not found")
    elif choice==3:
        if not contact:
            print("Empty contact book ")
        else:
            display_contact()
    elif choice==4:
        edit_contact=input("Enter the contact name to be edited: ")
        if edit_contact in contact:
            phone=input("Enter new mobile number: ")
            contact[edit_contact]=phone
            print("Contact Updated")
            display_contact()
        else:
            print("Name is not found")
    elif choice==5:
        del_contact=input("Enter contact to be deleted: ")
        if del_contact in contact:
            confirm=input("Do you want to delete : y/n")
            if confirm=="y" or confirm=="Y":
                contact.pop(del_contact)
            display_contact()
        else:
            print("Name is not found")
    else:
        break