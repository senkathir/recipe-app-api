from django.test import TestCase,Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        #nextline creates superuser in client that is created for test
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@gmail.com',
            password = 'adminpasswd'
        )
        self.client.force_login(self.admin_user)#forcibly login admin_user
        self.user = get_user_model().objects.create_user(
            email='test@gmail.com',
            password='Testpass123',
            name='any name'
        )

    def test_users_listed(self):
        """Test that users are listed on users page"""
        url = reverse('admin:core_user_changelist')#url for listing users
        #reverse is used so that changes in url need not to be made everywhere
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
        #assertion s brilliant enough to chk username from res(which is obj)

    def test_user_change_page(self):
        """Test that user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        #/admin/core/user/id->above url
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that the 'create user' page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)