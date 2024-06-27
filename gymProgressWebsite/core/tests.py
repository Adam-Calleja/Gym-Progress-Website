from django.test import TestCase, Client

from .models import GymUserManager, GymUser
from django.core.exceptions import ValidationError

class GymUserManagerTests(TestCase):
    def setUp(self):
        """
        Sets up the testing environment. 
        """

        self.gymUserManager = GymUser.objects 

    def test_create_user(self):
        """
        Tests the create_user method given that all fields are correct.

        The user should be saved.
        """

        self.gymUserManager.create_user(
            email = "test.email@email.com",
            username = "TestUser",
            password = "ThisIsATest1234"
        )

        user_exists = GymUser.objects.filter(username='TestUser').exists()

        self.assertTrue(user_exists)

        user = GymUser.objects.get(username='TestUser')

        self.assertEqual(user.email, 'test.email@email.com')
        self.assertTrue(user.check_password('ThisIsATest1234'))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_user_no_email(self):
        """
        Tests the create_user method given no email is entered.

        The user should not be saved. 
        A ValueError exception should be raised. 
        """

        with self.assertRaises(ValueError):
            self.gymUserManager.create_user(
                email = "",
                username = "TestUser",
                password = "ThisIsATest1234"
            )

        user_exists = GymUser.objects.filter(username='TestUser').exists()

        self.assertFalse(user_exists)  

    def test_create_user_no_username(self):
        """
        Tests the create_user method given no username is entered.

        The user should not be saved. 
        A ValueError exception should be raised. 
        """

        with self.assertRaises(ValueError):
            self.gymUserManager.create_user(
                email = "test.email@email.com",
                username = "",
                password = "ThisIsATest1234"
            )

        user_exists = GymUser.objects.filter(username='').exists()

        self.assertFalse(user_exists)

    def test_create_user_too_long_username(self):
        """
        Tests the create_user method given the username is longer than 150 
        characters.

        The user should not be saved. 
        A ValueError exception should be raised. 
        """

        username = "a" * 151

        user = self.gymUserManager.create_user(
                email = "test.email@email.com",
                username = username,
                password = "ThisIsATest1234"
            )
        
        with self.assertRaises(ValidationError) as context:
            user.full_clean()
        
        self.assertIn('Ensure this value has at most 150 characters', str(context.exception))

        user_exists = GymUser.objects.filter(username='').exists()

        self.assertFalse(user_exists)

    def test_create_user_username_150_characters(self):
        """
        Tests the create_user method given that all fields are correct.
        NOTE: In this test case, the username is 150 characters long. 

        The user should be saved.
        """

        username = "a" * 150

        self.gymUserManager.create_user(
            email = "test.email@email.com",
            username = username,
            password = "ThisIsATest1234"
        )

        user_exists = GymUser.objects.filter(username=username).exists()

        self.assertTrue(user_exists)

        user = GymUser.objects.get(username=username)

        self.assertEqual(user.email, 'test.email@email.com')
        self.assertTrue(user.check_password('ThisIsATest1234'))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_user_no_password(self):
        """
        Tests the create_user method given no password is entered.

        The user should not be saved. 
        A ValueError exception should be raised. 
        """

        with self.assertRaises(ValueError):
            self.gymUserManager.create_user(
                email = "test.email@email.com",
                username = "TestUser",
                password = ""
            )

        user_exists = GymUser.objects.filter(username='TestUser').exists()

        self.assertFalse(user_exists)

    def test_create_superuser(self):
        """
        Tests the create_superuser method given all input is correct. 

        The superuser should be saved.
        """

        self.gymUserManager.create_superuser(
            email = "test.email@email.com",
            username = "TestSuperUser",
            password = "ThisIsATest1234"
        )

        superuser_exists = GymUser.objects.filter(username='TestUser').exists()

        self.assertTrue(superuser_exists)

        superuser = GymUser.objects.get(username='TestUser')

        self.assertEqual(superuser.email, 'test.email@email.com')
        self.assertTrue(superuser.check_password('ThisIsATest1234'))
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

    def test_create_superuser_no_email(self):
        """
        Tests the create_superuser method given no email is entered.

        The superuser should not be saved. 
        A ValueError exception should be raised. 
        """

        with self.assertRaises(ValueError):
            self.gymUserManager.create_superuser(
                email = "",
                username = "TestUser",
                password = "ThisIsATest1234"
            )

        superuser_exists = GymUser.objects.filter(username='TestUser').exists()

        self.assertFalse(superuser_exists)  

    def test_create_superuser_no_username(self):
        """
        Tests the create_superuser method given no username is entered.

        The superuser should not be saved. 
        A ValueError exception should be raised. 
        """

        with self.assertRaises(ValueError):
            self.gymUserManager.create_superuser(
                email = "test.email@email.com",
                username = "",
                password = "ThisIsATest1234"
            )

        superuser_exists = GymUser.objects.filter(username='').exists()

        self.assertFalse(superuser_exists)

    def test_create_superuser_too_long_username(self):
        """
        Tests the create_superuser method given the username is longer than 150 
        characters.

        The superuser should not be saved. 
        A ValueError exception should be raised. 
        """

        username = "a" * 151

        superuser = self.gymUserManager.create_superuser(
                email = "test.email@email.com",
                username = username,
                password = "ThisIsATest1234"
            )
        
        with self.assertRaises(ValidationError) as context:
            superuser.full_clean()
        
        self.assertIn('Ensure this value has at most 150 characters', str(context.exception))

        superuser_exists = GymUser.objects.filter(username='').exists()

        self.assertFalse(superuser_exists)

    def test_create_superuser_username_150_characters(self):
        """
        Tests the create_superuser method given that all fields are correct.
        NOTE: In this test case, the username is 150 characters long. 

        The superuser should be saved.
        """

        username = "a" * 150

        self.gymUserManager.create_superuser(
            email = "test.email@email.com",
            username = username,
            password = "ThisIsATest1234"
        )

        superuser_exists = GymUser.objects.filter(username=username).exists()

        self.assertTrue(superuser_exists)

        superuser = GymUser.objects.get(username=username)

        self.assertEqual(superuser.email, 'test.email@email.com')
        self.assertTrue(superuser.check_password('ThisIsATest1234'))
        self.assertTrue(superuser.is_active)
        self.assertFalse(superuser.is_staff)
        self.assertFalse(superuser.is_superuser)

    def test_create_superuser_no_password(self):
        """
        Tests the create_superuser method given no password is entered.

        The superuser should not be saved. 
        A ValueError exception should be raised. 
        """

        with self.assertRaises(ValueError):
            self.gymUserManager.create_user(
                email = "test.email@email.com",
                username = "TestUser",
                password = ""
            )

        superuser_exists = GymUser.objects.filter(username='TestUser').exists()

        self.assertFalse(superuser_exists)


class RegisterViewTests(TestCase):
    def setUp(self):
        """
        Sets up the testing environment.
        """

        self.client = Client()
