#Kod pisany w programie Visual Studio Code

# Podstawy Python
import random
import string
import hashlib

class PasswordGeneratorMeta(type): # Użyta metaklasa
    def __new__(cls, name, bases, dct):
        def generate_password_hash(self, password):
            if self.hash_password:
                hasher = hashlib.sha256()
                hasher.update(password.encode('utf-8'))
                hashed_password = hasher.hexdigest()
                return hashed_password
            else:
                return password

        dct['generate_password_hash'] = generate_password_hash
        return super().__new__(cls, name, bases, dct)

class PasswordGenerator(metaclass=PasswordGeneratorMeta):  # Użyta klasa
    def __init__(self, length, hash_password=True):
        self.length = length
        self.hash_password = hash_password

    def generate_random_password(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(self.length))

class PasswordManager: # Użyta klasa
    def __init__(self):
        self.passwords = []

    def add_password(self, password):
        self.passwords.append(password)

    def save_passwords_to_file(self, filename):
        with open(filename, 'w') as file:
            for password in self.passwords:
                file.write(password + '\n')

def main():
    length = int(input("Podaj długość hasła: "))
    num_passwords = int(input("Podaj liczbę haseł do wygenerowania: "))
    filename = input("Podaj nazwę pliku do zapisu: ")
    hash_password = input("Czy chcesz haszować hasła? (t/n): ").lower() == 't'

    generator = PasswordGenerator(length, hash_password)
    manager = PasswordManager()

    for _ in range(num_passwords):
        password = generator.generate_random_password()
        manager.add_password(password)

    manager.save_passwords_to_file(filename)
    print("Hasło/a zapisano do pliku", filename)

if __name__ == "__main__":
    main()