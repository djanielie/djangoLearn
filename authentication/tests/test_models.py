from rest_framework.test import APITestCase
from authentication.models import User


class TestModel(APITestCase):

    def test_create_user(self):
        user = User.objects.create_user('Djanielie', 'djanielie@gmail.com', 'password123')
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, 'djanielie@gmail.com')
        self.assertFalse(user.is_staff)

    def test_create_superuser(self):
        user = User.objects.create_superuser('DjaniElie', 'djanielie@gmail.com', 'password123')
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, 'djanielie@gmail.com')
        self.assertTrue(user.is_staff)

    def test_raises_error_when_no_username_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user, username='', email='djanielie@gmail.com',
                          password='password123')

    def test_raises_error_message_when_no_username_supplied(self):
        with self.assertRaisesMessage(ValueError, 'The given username must be set'):
            User.objects.create_user(username='', email='djanielie@gmail.com', password='password123')

    def test_raises_error_when_no_email_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user, username='djanielie', email='',
                          password='password123')

    def test_raises_error_message_when_no_email_supplied(self):
        with self.assertRaisesMessage(ValueError, 'The given email must be set'):
            User.objects.create_user(username='djanielie', email='', password='password123')

    def test_create_staff_with_is_staff_status(self):
        with self.assertRaisesMessage(ValueError, 'Staff user must have is_staff=False.'):
            User.objects.create_user(username='djanielie', email='djanielie@gmail.com', password='password123',is_staff=True)

    def test_create_staff_with_super_user_status(self):
        with self.assertRaisesMessage(ValueError, 'Staff user must have is_superuser=False.'):
            User.objects.create_user(username='Djanielie', email='djanielie@gmail.com', password='password123',is_superuser=True)

    def test_create_super_user_with_is_staff_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_staff=True.'):
            User.objects.create_superuser(username='djanielie', email='djanielie@gmail.com', password='password123',is_staff=False)

    def test_create_super_user_with_super_user_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_superuser=True.'):
            User.objects.create_superuser(username='Djanielie', email='djanielie@gmail.com', password='password123',is_superuser=False)





