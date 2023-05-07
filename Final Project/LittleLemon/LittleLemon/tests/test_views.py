from django.test import TestCase
from Restaurant.views import MenuItemsView
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from Restaurant.models import Menu
from Restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setup(self):
        self.client = APIClient()
        self.salad = Menu.objects.create(Title = 'salad', Price = 5.75, Inventory=10)
        self.chease = Menu.objects.create(Title = 'chease', Price=5.75, Inventory = 5)
        self.pasta = Menu.objects.create(Title = 'pasta', price = 10.99, Inventory = 2)

    def test_getall(self):
        response = self.client.get(reverse('menu'))
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)