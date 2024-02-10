import unittest
from password_generator1 import PasswordGenerator, PasswordManager

class TestPasswordIntegration(unittest.TestCase):
    def test_password_generation_and_saving(self):
        generator = PasswordGenerator(10)
        manager = PasswordManager()

        for _ in range(5):
            password = generator.generate_random_password()
            manager.add_password(password)

        manager.save_passwords_to_file("test_integration_file.txt")


if __name__ == "__main__":
    unittest.main()
