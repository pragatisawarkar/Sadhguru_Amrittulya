from django.test import TestCase
from item.models import Item
from rest_framework.test import APITestCase
# Create your tests here.
class ItemTestCase(APITestCase):

    def SetUp(self):
        Item.objects.create(name='Tea', description='with crush',
                        price=30.0, item_image='images/IMG-20180129-WA0005.jpg' )

    def ItemDetail(self):
        url='http://127.0.0.1:8000/details/1/'
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)
        qs=Item.objects.filter(name='Tea')
        self.assertEqual(qs.count(),2)

    def add_Item(self):
        url='http://127.0.0.1:8000/add/'
        data={'name':'Tea', 'description':'with crush',
              'price':30.0, 'item_image':'images/IMG-20180129-WA0005.jpg'}
        response=self.client.get(url,data,format='json')
        self.assertEqual(response.status_code,201)

    def remove_item(self):
        url='http://127.0.0.1:8000/remove/1/'
        response=self.client.delete(url)
        self.assertEqual(response.status_code,204)