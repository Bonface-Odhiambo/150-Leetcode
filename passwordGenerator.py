import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == "__main__":
    password_length = int(input("Enter the desired password length: "))
    print("Generated password:", generate_password(password_length))
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    use_punctuation = input("Include punctuation? (yes/no): ").lower() == 'yes'

    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation

    if not characters:
        print("No character types selected, using default settings.")
        characters = string.ascii_letters + string.digits + string.punctuation

    print("Generated password:", generate_password(password_length))