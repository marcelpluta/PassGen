import unittest
from password_generator1 import PasswordGenerator, PasswordManager

class TestPasswordGenerator(unittest.TestCase):
    def test_generate_random_password(self):
        generator = PasswordGenerator(10)
        password = generator.generate_random_password()
        self.assertEqual(len(password), 10)

class TestPasswordManager(unittest.TestCase):
    def test_add_password(self):
        manager = PasswordManager()
        manager.add_password("test_password")
        self.assertIn("test_password", manager.passwords)

    def test_save_passwords_to_file(self):
        manager = PasswordManager()
        manager.passwords = ["test_password1", "test_password2"]
        manager.save_passwords_to_file("test_file.txt")

if __name__ == "__main__":
    unittest.main()