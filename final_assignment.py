import csv

def register():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    email = input("Enter your email address: ")
    
    with open("record.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password, email])
    print("Registration successful!")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    with open("record.csv", "r", newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            stored_username, stored_password, _ = row
            if username == stored_username and password == stored_password:
                print("Login successful!")
                return
        print("Invalid username or password.")

def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

