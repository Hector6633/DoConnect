from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages
from app.models import Contact_Info

class ContactViewTest(TestCase):

    def setUp(self):
        self.url = reverse('contact')  # make sure URL name = 'contact'
        
    def test_contact_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
        
    def test_contact_post_success(self):
        data = {
            'name': 'Rajeev',
            'email': 'rajeev@test.com',
            'number': '9876543210',
            'message': 'Test message'
        }

        response = self.client.post(self.url, data, follow=True)

        # Check redirect happened
        self.assertEqual(response.status_code, 200)

        # Check object created
        self.assertEqual(Contact_Info.objects.count(), 1)

        contact = Contact_Info.objects.first()
        self.assertEqual(contact.name, 'Rajeev')

        # Check success message
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Registered')