#!/usr/bin/env python3

def main():
    # Display the registration form header
    print("Registration Form")
    print()
    
    # Get input from the user
    first_name = input("First name: ")
    last_name = input("Last name: ")
    birth_year = input("Birth year: ")
    
    # Generate the user's full name and temporary password
    full_name = f"{first_name} {last_name}"
    temp_password = f"{first_name}*{birth_year}"
    
    # Display the completion message
    print()
    print(f"Welcome {full_name}!")
    print("Your registration is complete.")
    print(f"Your temporary password is: {temp_password}")

if __name__ == "__main__":
    main()