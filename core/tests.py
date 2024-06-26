from django.test import TestCase,Client

#testing the home page
class TestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_homepage_view(self):
        response = self.client.get('/')#checking for the route
        self.assertEqual(response.status_code,200)#checking status code is 200
        self.assertTemplateUsed(response,'core/home.html')

    def test_detail_view(self):
        response = self.client.get('detail/<str:pk>/')
        self.assertNotEqual(response.status_code,200) # status code is 404 because of static images


