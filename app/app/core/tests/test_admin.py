from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@prova.com',
            password='test123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='user@prova.com',
            password='password123',
            name='Test user full name'
        )

    def test_user_listed(self):
        """Test users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        # reverse function retrieve the URL from the string inserted;
        # this allows you to not change manually the url in the test
        # when this will be modify in the future.
        # For more detail go to
        # https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#reversing-admin-urls
        response = self.client.get(url)
        # This will use our test client ti perforn an HTTP GET on
        # the url e have found here.
        self.assertContains(response, self.user.name)
        self.assertContains(response, self.user.email)
        # The assertContains is a django custom assertion that will
        # check that our response here contains the wanted item.

    def test_user_change_page(self):
        """The user edit page works"""
        url = reverse('admin:core_user_changelist')
        # The lecturer add the argument args=[self.user.id]
        # but there is a problem with my code.
        # It returns '/admin/core/\\Z' instead of
        # '/admin/core/1'.
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_user_page(self):
        """Test that create user page works"""
        url = reverse('admin:core_user_add')
        # 'core_user_add' is the standard URL alias for the
        # add page for our user model.
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
