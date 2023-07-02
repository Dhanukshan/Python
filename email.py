def generate_password(email_id):
    # Extract username from email ID
    username = email_id.split('@')[0]

    # Generate password as username followed by reverse uppercase of the username
    password = username[::-1].upper()

    return username, password


if __name__ == "__main__":
    email_id = input("Enter the email id: ")
    username, password = generate_password(email_id)

    print("Username -", username)
    print("Password -", password)
