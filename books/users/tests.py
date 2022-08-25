from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.
class CustomUserTest(TestCase):
    def test_user_create(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="testuser", email="test@email.com", password="testpass123"
        )

        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "test@email.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username="testsuperuser",
            email="supertest@email.com",
            password="supertestpass123",
        )
        self.assertEqual(user.username, "testsuperuser")
        self.assertEqual(user.email, "supertest@email.com")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
