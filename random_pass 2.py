import random
import string

print("Welcome to Random Password Generator")
def main():
    length = int(input("Enter the length of the password:"))
    num_passwords = int(input("Enter the number of passwords to generate: "))
    filename = input("Enter the name of the file to save the passwords to: ")

    with open(filename, 'w') as file:
        for i in range(num_passwords):
            lower=string.ascii_lowercase
            upper=string.ascii_uppercase
            dig=string.digits
            symbol=string.punctuation
            combine=lower+upper+dig+symbol
            p=random.sample(combine, length)
            password="".join(p)
            print(password)
            file.write(password + "\n")

if __name__ == '__main__':
    main()
