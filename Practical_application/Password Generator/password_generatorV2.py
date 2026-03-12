import secrets
import string
import datetime

def generate_and_save_password():
    # Define character pool
    chars = string.ascii_letters + string.digits + string.punctuation
    filename = "passwords.txt"
    
    print("--- Secure Password Generator & Vault ---")
    
    while True:
        try:
            length_input = input("\nEnter password length (or 'q' to quit): ").lower()
            if length_input == 'q':
                break
                
            length = int(length_input)
            label = input("What is this password for? (e.g., Gmail, WiFi): ")
            
            # Generate secure password
            password = "".join(secrets.choice(chars) for _ in range(length))
            
            # Get current timestamp
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Save to file
            with open(filename, "a") as file:
                file.write(f"{timestamp} | {label:15} | {password}\n")
            
            print(f" Generated and saved: {password}")
            print(f"Stored in {filename}")
            
        except ValueError:
            print(" Please enter a valid number for the length.")

if __name__ == "__main__":
    generate_and_save_password()