from django.test import TestCase
from django.urls import reverse


class StoreViewTest(TestCase):

    def test_collection_list_page_status(self):
        url = reverse('store:collection_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
