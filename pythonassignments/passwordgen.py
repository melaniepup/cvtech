import random  
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''
    for i in range(length):
        password += random.choice(characters)

    return password

def generate_multiple_passwords():
    length = int(input("Enter the desired password length: "))
    num_passwords = int(input("Enter the desired password count: "))
    for i in range(num_passwords):
        print(f'password {i + 1} is {generate_password(length)}\n')    

if __name__ == '__main__':
    generate_multiple_passwords()